# Śnieżka SkiPass – system rezerwacji i zakupu karnetów narciarskich

## 1. Zespół
* **Nazwa zespołu:** [Zespół Śnieżka]
* **Skład zespołu:**
  * [Michał Minda] – nr indeksu: [175641], GitHub: @[mmminda]
  * [Radomił Pakuła] – nr indeksu: [xxxxxx], GitHub: @[login_github]
* **Grupa laboratoryjna:** [Grupa 1]

---

## 2. Idea i problem
Sieć stacji narciarskich „Śnieżka” zmaga się z problemem długich kolejek do kas stacjonarnych, szczególnie w weekendy oraz w szczycie sezonu zimowego. Obecnie turyści muszą osobiście stać w kolejce przy kasie, aby zapoznać się z cennikiem oraz kupić karnet, co powoduje frustrację i skraca czas faktycznej jazdy na stoku. Jednocześnie pracownicy kas są przeciążeni ręczną obsługą standardowych zapytań i sprzedażą podstawowych pakietów. Naszym rozwiązaniem jest prosta aplikacja internetowa umożliwiająca klientom przeglądanie aktualnej oferty karnetów i rezerwację wybranego pakietu online przed przyjazdem na stok. Zastosowanie systemu pozwoli rozładować kolejki przy kasach i odciążyć personel stacji. Klient zyska wygodny wgląd w cennik, szybkie wyliczenie kosztu dla swojej grupy oraz możliwość zarządzania swoimi karnetami w jednym miejscu z poziomu przeglądarki lub telefonu.

---

## 3. Użytkownicy i scenariusz użycia
* **Główna grupa odbiorców:** Klienci indywidualni oraz grupy turystów planujące pobyt na stacji narciarskiej „Śnieżka”.
* **Scenariusz użycia:** 
  Klient wchodzi na stronę główną aplikacji i przegląda aktualny cennik dostępnych karnetów (np. Normalny, Ulgowy, Dziecięcy). Następnie przechodzi do formularza zakupu, wybiera interesujący go rodzaj karnetu, wskazuje datę ważności i zatwierdza rezerwację. System automatycznie wylicza kwotę do zapłaty, zapisuje zamówienie w bazie danych i generuje unikalny kod karnetu. Na koniec klient przechodzi do widoku „Moje karnety”, gdzie widzi swój aktywny karnet gotowy do okazania na stacji (lub może go anulować w razie zmiany planów).

---

## 4. Zakres funkcjonalny

Zgodnie z założeniami dla pierwszej wersji (v1), w ramach MVP realizujemy 3 kluczowe i spójne funkcjonalności pozwalające na pełny obieg zamówienia.

| ID | Funkcjonalność | Zakres |
| :--- | :--- | :--- |
| **F01** | Użytkownik może przeglądać listę dostępnych karnetów wraz z ich aktualną ceną. | **MVP** |
| **F02** | Użytkownik może zarezerwować/kupić wybrany karnet na wskazany dzień (wygenerowanie karnetu ze statusem „Aktywny”). | **MVP** |
| **F03** | Użytkownik może przeglądać swoje zakupione karnety oraz anulować wybrany aktywny karnet. | **MVP** |
| **F04** | Użytkownik może zarezerwować usługę dodatkową (wypożyczenie sprzętu lub lekcję z instruktorem). | Rozszerzenie (v2) |
| **F05** | Administrator może dodawać nowe pozycje do oferty i edytować ceny karnetów. | Rozszerzenie (v2) |

---

## 5. Poza zakresem (Out of Scope dla wersji v1)
Poniższe elementy z szerokiej koncepcji biznesowej zostają celowo wyłączone z pierwszej wersji aplikacji:
* **Integracja sprzętowa z fizycznymi bramkami RFID na stoku** – system wygeneruje jedynie cyfrowy kod karnetu w bazie danych, bez komunikacji ze sterownikami bramek.
* **Zewnętrzni operatorzy płatności (BLIK / terminale płatnicze) i drukarki fiskalne** – zakup w wersji v1 będzie opierał się na symulowanym zatwierdzeniu zamówienia w systemie.
* **Generowanie raportów podatkowych (JPK) dla Urzędu Skarbowego oraz system zgłoszeń GOPR.**

---

## 6. Organizacja współpracy
* **Wstępny podział zadań:**
  * **[Michał]:** Konfiguracja repozytorium GitHub, opracowanie opisu idei projektu, scenariusza użycia oraz przygotowanie struktury bazy danych w kolejnych etapach.
  * **[Radomił]:** Konfiguracja przestrzeni w LaboChat.com, spisanie zakresu funkcjonalnego (MVP i rozszerzeń) oraz przygotowanie szkiców widoków interfejsu.
* **Sposób kontaktu:** Bieżąca komunikacja przez komunikator (Discord / Messenger) oraz wpisy w przestrzeni projektu na LaboChat.com.
* **Zasada zapisywania ustaleń:** Wszystkie wiążące decyzje projektowe oraz postępy w zadaniach są odnotowywane na tablicy w LaboChat.com, a dokumentacja techniczna jest na bieżąco aktualizowana bezpośrednio w repozytorium GitHub.

---

## 7. Odnośniki
* **Repozytorium GitHub:** [https://github.com/mmminda/InzOprog]
* **Przestrzeń projektu w LaboChat.com:** [xxx]
