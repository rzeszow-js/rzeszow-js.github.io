.. presentation:: Nov 30, 2017
   :title: Deploying node js applications
   :tags: devops, javascript, ansible
   :category: devops

   # Deploying NodeJS application

   ### Classic way

   <small>[@voronenko](https://github.com/voronenko)</small>

   ---



   ## Good habits

   * Code workflow
   * Code testing
   * Code architecture

   ---

   ## Code worflow strategies

   * Feature Branch Workflow
   * Gitflow Workflow
   * better, if not a centralized workflow (vss, svn)

   ---

   ## Code testing

   * Unit testing
   * E2e testing

   ---

   ## Adequate config organization

   * common part +
   * environment overrides +
   * instance overrides +
   * local overrides


   ---

   ## Database structure & data migrations


   * Exists for most of node ORMs (ex. Sequelize)
   * Exists for most of the databases
   * can be different from application core framework itself
   * nice fact: if you have tests - most likely you have migrations

   ---

   ## Infrastructure as a code

   deployment logic is developed together with application

   * you can recreate exactly the same environment than year ago.
   * you can recreate exactly the same environment as commit XX


   ---

   ## Application logging

   * At least readable
   * Cooler if supports decoupling, multiple transports, different levels (winstonjs)

   ---

   ## Application stats reporting

   * At least healthcheck
   * Cooler if supports reporting characteristics (Prometheus or similar)

   ---

   ## Application faults reporting

   * At least readable into log
   * Cooler if supports reporting to tools like Sentry, NewRelic or similar


   ---

   ## Where we deploy nodejs nowadays ?

   Everywhere

   * PAAS (Amazon elastic beanstalk, Heroku)

   * Containers (Kubernetes, Docker, Openshift, Swarm, etc)

   * Shared hosting

   * Own host (bare metal, vps like digital ocean instance , Amazon ec2)

   * More...

   ---

   ## Threats - quite low, but

   Nodejs	» Nodejs	: Vulnerability Statistics

   ---

   ## BUT

   <!-- .slide: data-background="auto.jpg" -->

   ---

   ## BUT

   > “ The U.S. Department of Homeland Security (DHS) states that 90 percent of security incidents result from exploits against defects in software.  That's a big statement - and it implies that poor software development may be the biggest cyber threat of all.“

   ---

   # Classic server deployment


   ## Deployment phases

   * Box preparation for deployment
   * Installation of the core components (web server, language runtime, SSL support, libs)
   * Initial application setup flow
   * Update application setup flow
   * Proper box securing

   ---

   ## Disclaimer

   > "Almost since 2009, being not drunk , no-one deploys commercial applications manually"

   ---

   ## CD

   <!-- .slide: data-background="typical_cd.png" -->

   ---

   ## Offtopic

   In 2017 known players in automation are:
   * OpsCode Chef (ruby, and ruby in custom logic, master-slave concept)
   * Puppet (ruby, but unfortunately own configuration language, requires client)
   * Salt Stack  (python, master-slave concept)
   * Ansible (python, and python in custom logic. Client less. Winner in learning curve)


   ---

   ## Box preparation for deployment

   > “ A Security Technical Implementation Guide (STIG) is a cybersecurity methodology for standardizing security within networks, servers logical designs to enhance overall security. Guides, when implemented, enhance security for software, hardware, logical architectures to reduce vulnerabilities."

   ---

   ## Some advises

   * Minimize Software to Minimize Vulnerability
   * One Network Service Per System or VM Instance
   * Keep Linux Kernel and Software Up to Date
   * Proper secure software (and hardware)
   * More ...

   ---

   ## Core components setup: webserver

   * Nginx
   * Apache
   * but not limited to...

   ---

   ## Core components setup: Language runtime

   * Global NodeJS install

   or

   * multiple node versions (nvm)?

   ---

   ## Core components: DB

   * Mysql or clone
   * Postgresql
   * MongoDB
   * but not limited to ...

   ---


   ## Application: what do we need ?

   Way to ...

   * start/stop application (and better than forever, nohup , etc)
   * restart application in case of failure
   * monitor status (healthcheck)
   * Serve statics using webserver

   ---


   ## Application: service

   * Provided by OS (upstart, systemd)
   * "Applications server" (supervisord, passenger, pm2)

   ---

   ## Application: monitoring

   note: open port is not enough

   * application health check
   * advanced: custom figures reporting

   ---

   ## "Development meat" (tm)

   <!-- .slide: data-background-image="https://media.giphy.com/media/vl8ncD72EnhoA/giphy.giff" data-background-color="#000000" -->


   ---

   ## Upstart (older way)

   ```shell
   description "Your App"
   start on runlevel [2345]
   stop on runlevel [016]

   respawn
   console log
   setuid {{project_app_user}}
   setgid {{project_app_user}}

   env HOME={{project_directory}}
   env NODE_ENV=production

   exec start-stop-daemon --chdir ${HOME} --start --make-pidfile
   --pid=/var/run/{{project_upstart_name}}.pid
   --exec {{npm_path_detected}}/node -- bin/app.js {{params}}

   ```

   ---

   ## SystemD (most of modern OS)

   ```shell
   [Unit]
   After=network.target
   Requires=network.target

   [Service]
   Environment=NODE_ENV=production
   Environment=HOME={{project_directory}}
   ExecStart={{npm_path_detected}}/node -- bin/www {{extra_project_params}}

   WorkingDirectory={{project_directory}}
   PIDFile=/var/run/yourapp/{{project_upstart_name}}.pid

   User={{project_user}}
   Group={{project_user}}

   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

   ---

   ## SupervisorD (mostly ex py guys :)

   ```shell
   [program:my-api]
   command={{npm_path_detected}}/node -- bin/www {{extra_project_params}}
   autostart=true
   autorestart=true
   environment=NODE_ENV=production
   stderr_logfile=/var/log/myapi.err.log
   stdout_logfile=/var/log/myapi.out.log
   user=myuser

   [eventlistener:httpok]
   command=httpok -p my-api http://localhost:3000/healthcheck
   events=TICK_5
   ```


   ---

   ## Bind to the nginx

   ```conf
     location / {
       try_files $uri @backend;
     }

     location @backend {
       proxy_pass http://127.0.0.1:{{project_node_port}};
       proxy_redirect off;
       proxy_set_header Host $host;
     }

     location /socket.io/ {
       proxy_pass http://127.0.0.1:{{project_node_port}};
       proxy_http_version 1.1;
       proxy_set_header Upgrade $http_upgrade;
       proxy_set_header Connection "upgrade";
     }

   ```

   ---

   ## Nodejs code deployment


   * Pre-created artifact vs repository checkout at tag
   * Node modules included in artifact vs running npm install on server
   * Rolling / blue green deployment - rollback strategy?

   <small>** "Zero downtime deployment" in most cases is science fiction</small>

   ---


   ## Links

   * Deployment https://github.com/Voronenko/devops-node-app-demo
   * Ansible https://www.ansible.com/
   * Gitflow https://github.com/nvie/gitflow
   * PM2 https://github.com/Unitech/pm2
   * Monit https://github.com/arnaudsj/monit


   ---


   ## Thanks

   Questions ?

   > “For years there has been a theory that millions of monkeys typing at random on millions of typewriters would reproduce the entire works of Shakespeare. The Internet has proven this theory to be untrue.”
