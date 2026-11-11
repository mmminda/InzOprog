# Śnieżka SkiPass – system rezerwacji i zakupu karnetów narciarskich

## 1. Zespół
* **Nazwa zespołu:** Zespół śnieżka
* **Skład zespołu:**
  * Michał Minda – nr indeksu: 175641, GitHub: @mmminda
  * Radomił Pakuła – nr indeksu: 169474, GitHub: @pakular
* **Grupa laboratoryjna:** Grupa nr. 1

---

## 2. Idea i problem
Sieć stacji narciarskich „Śnieżka” zmaga się z problemem długich kolejek do kas stacjonarnych, szczególnie w weekendy oraz w szczycie sezonu zimowego. Obecnie turyści muszą osobiście stać w kolejce przy kasie, aby zapoznać się z cennikiem oraz kupić karnet, co powoduje frustrację i skraca czas faktycznej jazdy na stoku. Jednocześnie pracownicy kas są przeciążeni ręczną obsługą standardowych zapytań i sprzedażą podstawowych pakietów. Naszym rozwiązaniem jest prosta aplikacja internetowa umożliwiająca klientom przeglądanie aktualnej oferty karnetów i rezerwację wybranego pakietu online przed przyjazdem na stok. Zastosowanie systemu pozwoli rozładować kolejki przy kasach i odciążyć personel stacji. Klient zyska wygodny wgląd w cennik, szybkie wyliczenie kosztu dla swojej grupy oraz możliwość zarządzania swoimi karnetami w jednym miejscu z poziomu przeglądarki lub telefonu.

---

## 3. Użytkownicy i scenariusz użycia
* **Główna grupa odbiorców:** Klienci indywidualni oraz grupy turystów planujące pobyt na stacji narciarskiej „Śnieżka”.
* **Tryb demonstracyjny (v1):** Aplikacja w wersji v1 działa w kontekście lokalnego użytkownika demonstracyjnego nr 1 (`Jan Nowak`, `jan.nowak@example.com`), który jest automatycznie tworzony podczas inicjalizacji bazy danych.
* **Scenariusz użycia:** 
  Klient wchodzi na stronę główną aplikacji (W01) i przegląda aktualny cennik dostępnych karnetów (Normalny, Ulgowy, Dziecięcy). Następnie przechodzi do formularza zakupu (W02), wybiera interesujący go rodzaj karnetu, wskazuje datę ważności i zatwierdza rezerwację. System waliduje poprawność daty oraz brak kolizji, zapisuje zamówienie w bazie SQLite i generuje unikalny kod QR karnetu. Na koniec klient przechodzi do widoku „Moje karnety” (W03), gdzie widzi swój aktywny karnet lub może go anulować.

---

## 4. Zakres funkcjonalny

| ID | Funkcjonalność | Zakres |
| :--- | :--- | :--- |
| **F01** | Użytkownik może przeglądać listę dostępnych karnetów wraz z ich aktualną ceną. | **MVP (Zrealizowane w v1)** |
| **F02** | Użytkownik może zarezerwować/kupić wybrany karnet na wskazany dzień (wygenerowanie karnetu ze statusem „Aktywny”). | **MVP (Zrealizowane w v1)** |
| **F03** | Użytkownik może przeglądać swoje zakupione karnety oraz anulować wybrany aktywny karnet. | **MVP (Zrealizowane w v1)** |
| **F04** | Użytkownik może zarezerwować usługę dodatkową (wypożyczenie sprzętu lub lekcję z instruktorem). | Rozszerzenie (v2) |
| **F05** | Administrator może dodawać nowe pozycje do oferty i edytować ceny karnetów. | Rozszerzenie (v2) |

---

## 5. Poza zakresem (Out of Scope dla wersji v1)
* **Integracja sprzętowa z fizycznymi bramkami RFID na stoku** – system generuje cyfrowy kod karnetu w bazie danych, bez komunikacji ze sterownikami bramek.
* **Zewnętrzni operatorzy płatności (BLIK / terminale płatnicze) i drukarki fiskalne** – zakup w wersji v1 opiera się na lokalnym zatwierdzeniu zamówienia w systemie.
* **Generowanie raportów podatkowych (JPK) dla Urzędu Skarbowego oraz system zgłoszeń GOPR.**

---

## 6. Instrukcja uruchomienia lokalnego i inicjalizacji bazy (v1)

Wymagany zainstalowany **Python 3** (zalecana wersja 3.10+). Otwórz terminal w głównym katalogu projektu i wykonaj polecenia odpowiednie dla swojego systemu operacyjnego:

### Windows (PowerShell):
```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m flask --app app init-db
.\.venv\Scripts\python.exe -m flask --app app run
