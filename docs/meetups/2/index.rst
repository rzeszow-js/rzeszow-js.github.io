.. _meetup2:

Meetup #2: Let's meet each other and talk!
==========================================

.. container:: container

    .. container:: row me-row schedule

        .. container:: col-md-12

            .. raw:: html

                <!-- Nav tabs -->
                <ul class="nav nav-tabs" role="tablist">
                <li role="presentation" class="active"><a href="#talk-1" aria-controls="home" role="tab" data-toggle="tab">Talk 01 <small class="hidden-xs">(30<sup>th</sup>, November)</small></a></li>
                <li role="presentation"><a href="#talk-2" aria-controls="profile" role="tab" data-toggle="tab">Talk 02 <small class="hidden-xs">(30<sup>th</sup>, November)</small></a></li>
                </ul>

                <!-- Tab panes -->
                <div class="tab-content">
                <div role="tabpanel" class="tab-pane fade in active" id="talk-1">
                    <div class="row">
                    <div class="col-md-6">
                        <div class="media">
                        <div class="media-left">
                            <a href="#">
                            <img class="media-object" src="/_static/img/speaker-slawek.png" alt="...">
                            </a>
                        </div>
                        <div class="media-body">
                            <h4 class="media-heading">19:00 to 19:30</h4>
                            <h5>HyperProxy - Backend Tool For Front-End Developers</h5>
                            <p></p>
                        </div>
                        </div>
                    </div>
                    </div>
                </div>
                <div role="tabpanel" class="tab-pane fade" id="talk-2">
                    <div class="row">
                    <div class="col-md-6">
                        <div class="media">
                        <div class="media-left">
                            <a href="#">
                            <img class="media-object" src="/_static/img/speaker-slavik.png" alt="...">
                            </a>
                        </div>
                        <div class="media-body">
                            <h4 class="media-heading">19:30 to 20:00</h4>
                            <h5>Classic Way On Deploying NodeJs Application</h5>
                            <p></p>
                        </div>
                        </div>
                    </div>
                    </div>
                </div>

Talk 1:  hyperProxy - backend tool for frontend developers
----------------------------------------------------------

Co to jest hyperProxy?
======================

hyperProxy, to server napisany w node.js. Wykorzystuje on mechanizm
ataku `MITM <https://pl.wikipedia.org/wiki/Atak_man_in_the_middle>`__
aby przechwytywać requesty i w zależności od zdefiniowanych reguł
zwracać rezultat w odpowiedni sposób.

Jakie są wymagania?
===================

`node.js <https://nodejs.org/en/>`__ - w wersji 4.x.x lub nowszy moduł
`hyperProxy <https://github.com/Hypermediaisobar/hyperProxy>`__ - do
ściągnięcia z githuba przeglądarka (np. Google Chrome)

Kiedy warto używać?
===================

-  Kiedy z jakiegoś powodu nie masz dostępu do backendu a potrzebujesz
   móc przygotować poprawki dla frontendu,
-  Kiedy na produkcji pojawi się błąd, którego nie możesz odtworzyć w
   środowisku lokalnym i potrzebujesz debugować kod produkcyjny
   (zminifikowany),
-  Kiedy jako front-end developer nie chcesz mieć zainstalowanych 5
   serverów bazodanowych, JDK, .NET SDK, PHP, Python, Go, Ruby i wielu
   innych, a jednocześnie chcesz móc zmienić dowolne elementy warstwy
   działającej w przeglądarce,
-  Kiedy z jakiegoś powodu klient nie może dać Ci dostępu do backendu
   (lub też jego odtworzenie jest zbyt skomplikowane)
-  Kiedy chcesz zacząć pracę mimo, że klient nie dał Ci jeszcze dostępu
   do repozytorium

Jak tego użyć?

:ref:`Read more <hyperproxy>`

For pdf, please see :download:`hyperProxy <talk1/hyperproxy.pdf>`.


Talk 2:  Classic Way On Deploying NodeJs Application
----------------------------------------------------

Presentation: :ref:`check it out <meetup_2_2>`

Demo node application: https://github.com/voronenko-p/node-sample

Provisioning project: https://github.com/Voronenko/devops-node-box-template


.. toctree::
   :hidden:

   talk1/index.rst
   talk2/index.rst
