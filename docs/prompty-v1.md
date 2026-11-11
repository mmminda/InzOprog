# Dokumentacja promptów i decyzji zespołu – Iteracja v1

## 1. Użyte narzędzie AI
* **Wybrany czat AI:** Gemini (Google) – wariant bezpłatny (`gemini.google.com`).
* **Zadanie rozgrzewkowe:** Wysłaliśmy zapytanie wyjaśniające rolę widoku, serwera i bazy danych, a następnie przełożyliśmy je na architekturę naszego systemu zakupu karnetów.

---

## 2. Kluczowe prompty użyte podczas tworzenia v1

### Prompt P1 – Wybór technologii
> „Pracujemy we dwoje nad projektem Śnieżka SkiPass – system rezerwacji i zakupu karnetów narciarskich. Cel v1: przejrzenie oferty, zakup karnetu na wybrany dzień i możliwość jego anulowania. Widoki: W01 Oferta karnetów, W02 Zakup karnetu, W03 Moje karnety. Dane: tabele uzytkownik, oferta, karnet (relacje 1:N). Funkcje MVP: F01 przegląd oferty, F02 zakup karnetu, F03 lista i anulowanie karnetu. Zaproponuj prosty zestaw technologii do uruchomienia lokalnie bez płatnych usług (Python + Flask + SQLite), wyjaśnij role składników i uzasadnij wybór.”

### Prompt P2 i P3 – Szkielet aplikacji i widoki zgodne ze szkicami
> „Przygotuj szkielet lokalnej aplikacji Śnieżka SkiPass v1: HTML/CSS, Python 3, Flask i SQLite przez sqlite3. Plik startowy: app.py. Widoki: W01 oferta karnetów, W02 formularz zakupu (wybór oferty i daty ważności), W03 moje karnety. Dodaj nawigację, etykiety pól i miejsca na komunikaty sukcesu oraz błędów. Użyj lokalnego użytkownika demonstracyjnego nr 1 (Jan Nowak). Zwróć pełną zawartość plików, requirements.txt, .gitignore oraz instrukcję startu.”

### Prompt P4 – Baza danych SQLite
> „Dodaj trwałą bazę SQLite przez moduł sqlite3 zgodnie z mapą projektu: uzytkownik(id, imie, email), oferta(id, nazwa, cena, opis), karnet(id, uzytkownik_id, oferta_id, data_waznosci, kod_qr, status). Oznacz PK i FK oraz włącz kontrolę kluczy obcych (PRAGMA foreign_keys = ON). Używaj zapytań parametryzowanych (?). Dodaj polecenie flask --app app init-db oraz automatyczne tworzenie 3 ofert startowych i użytkownika demo nr 1. Ponowny start aplikacji ma zachowywać dane.”

### Prompt P5 – Implementacja funkcjonalności MVP (F01, F02, F03)
> „Na obecnym kodzie wykonaj kolejno: F01 wyświetlanie cennika z bazy w W01, F02 utworzenie rezerwacji karnetu w W02 z wygenerowaniem kodu QR i zapisem do bazy oraz F03 anulowanie aktywnego karnetu użytkownika demo nr 1 w W03. Sprawdzaj dane na serwerze: wymagane pola, data ważności nie może być z przeszłości (wybrana_data >= dzisiaj) oraz brak kolizji aktywnego karnetu tego samego typu na ten sam dzień dla tego użytkownika. Anulowanie zmienia status na 'Anulowany' i zwalnia termin.”

---

## 3. Decyzje zespołu i własne poprawki w kodzie
1. **Zintegrowanie szablonów w jednym pliku `templates/layout.html`:** Zdecydowaliśmy się umieścić strukturę trzech widoków (W01, W02, W03) w jednym spójnym szablonie sterowanym parametrem `view`, co wyeliminowało duplikację kodu paska nawigacji oraz sekcji wyświetlania komunikatów (`flash`).
2. **Automatyczna inicjalizacja bazy danych:** Oprócz osobnej komendy terminalowej `flask --app app init-db`, dodaliśmy wywołanie `init_db()` przy starcie pliku `app.py` (z użyciem `CREATE TABLE IF NOT EXISTS`), dzięki czemu aplikacja nie zwraca błędu przy pierwszym uruchomieniu, jeśli użytkownik zapomni wcześniej zainicjować bazę.
3. **Przekazywanie wybranego karnetu z W01 do W02:** Dopracowaliśmy przekazywanie parametru `?oferta_id=` w adresie URL po kliknięciu przycisku „Wybierz i kup” w widoku W01, aby w formularzu W02 odpowiedni karnet był od razu domyślnie zaznaczony.
