hyperProxy -
============

backend tool for frontend developers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Co to jest hyperProxy?
----------------------

hyperProxy, to server napisany w node.js. Wykorzystuje on mechanizm
ataku `MITM <https://pl.wikipedia.org/wiki/Atak_man_in_the_middle>`__
aby przechwytywać requesty i w zależności od zdefiniowanych reguł
zwracać rezultat w odpowiedni sposób.

Jakie są wymagania?
-------------------

-  `node.js <https://nodejs.org/en/>`__ - w wersji 4.x.x lub nowszy,
-  moduł `hyperProxy <https://github.com/Hypermediaisobar/hyperProxy>`__
   - do ściągnięcia z githuba,
-  przeglądarka (np. Google Chrome)

Kiedy warto używać?
-------------------

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
--------------

Na początek ściągnij repozytorium
`hyperProxy <https://github.com/Hypermediaisobar/hyperProxy>`__ ze
strony autora. Jeśli ściągnąłeś zip-a - rozpakuj go. W katalogu
'example' znajdziesz plik 'example.js', który zawiera definicję 2
obiektów: - overrides, - settings

Pierwszy z nich odpowiada za 'reguły nadpisywania' (zestaw funkcji
określających jak się zachować gdy URL wpisany w przeglądarce
koresponduje z ustawieniami w funkcji). Moduł pozwala na pisanie
własnych funkcji, jednak zawiera również kilka predefiniowanych, które z
pomocą regex-ów w praktyce pozwalają na obsługę 99% requestów. Drugi
plik to ustawienia samego servera proxy. W najprostszej wersji mówimy na
jakim porcie ma działać, ewentualnie podajemy ścieżki do certyfikatów
niezbędnych do obsługi ruchu po https. Ostatnia rzecz, której
potrzebujemy, to certyfikat SSL dla lokalnej maszyny. Informacje o tym
jak go wygenerować znajdziecie zarówno na stronie projektu
`hyperProxy <https://github.com/Hypermediaisobar/hyperProxy>`__ jak i na
`milionie innych stron w internecie <http://bfy.tw/FcqJ>`__, więc nie
będę się nad tym rozwodził.

Szczegółowe ustawienia dotyczące konfiguracji narzędzia znajdziecie w
pliku README.md projektu hyperProxy. W samym narzędziu zdefiniowałem
konfigurację proxy, która przepuszcza cały ruch (http i https) przez
:8000 (domyślne ustawienia z hyperProxy).

Kolejną rzecz, którą należy skonfigurować to ustawienia przeglądarki
związane z używaniem serwera proxy. Aby ułatwić sobie życie w tym
obszarze używam rozszerzenia do Chrome'a - `Proxy
SwitchyOmega <https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif>`__.

Gdy uruchomimy server - magia zaczyna działać. No tak ... ale też szybko
dostrzeżemy pierwsze problemy. W szczególności może być nim ruch po
https. Wiele CDNów lub API blokuje ruch "podrobionych" certyfikatów z
użyciem
`HSTS <https://pl.wikipedia.org/wiki/HTTP_Strict_Transport_Security>`__.
Na szczęście finalnie to nasza przeglądarka decyduje o tym, czy i jak
obsłużyć daną zawartość a nie dostawca. Aby "zmusić" Chrome'a do
poprawnej współpracy z w takiej sytuacji należy `włączyć ustawienia w
przeglądarce związane z obsługą nieprawidłowych
certyfikatów <chrome://flags/#allow-insecure-localhost>`__.

Ostatnią rzeczą jest uruchomienie przeglądarki. W przypadku Chrome'a
potrzebne jest dodanie dodatkowej flagi, więc finalnie polecenie
uruchamiające wygląda w moim przypadku następująco:

.. code:: sh

    "<sciezka-do-przegladarki-chrome>\chrome.exe" --ignore-certificate-errors

Pytania?
--------

Jeśli masz jakieś pytania - `skontaktuj się ze
mną <https://github.com/slawomir-pasko>`__, jeśli tylko będę w stanie na
pewno pomogę.

Podziękowania
-------------

-  Dla `Marcina <https://github.com/ahwayakchih>`__, który kilka lat
   temu pokazał mi to narzędzie,
-  Dla `Vyacheslava <https://github.com/Voronenko>`__, który zmotywował
   mnie do tego abym powiedział kilka słów na meetup'ie,
-  Wszystkich obecnych na meetup'ie :)

