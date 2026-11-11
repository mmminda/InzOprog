# Wybór technologii – Śnieżka SkiPass (v1)

## 1. Zestawienie wybranych narzędzi i ich ról

| Obszar | Wybrane rozwiązanie i wersja | Rola w projekcie |
| :--- | :--- | :--- |
| **Widoki (Frontend)** | HTML5, CSS3 (szablony Jinja2) | Prezentacja cennika (W01), formularza zakupu (W02) oraz listy karnetów klienta (W03). |
| **Serwer (Backend)** | Python 3.11+ oraz Flask 3.0.3 | Obsługa żądań HTTP, routing widoków, walidacja dat i kolizji karnetów oraz logika biznesowa. |
| **Baza danych** | SQLite 3 (moduł `sqlite3`) | Trwały zapis użytkowników, oferty i karnetów w lokalnym pliku `sniezka.db` z kontrolą kluczy obcych. |
| **Praca zespołu** | VS Code, Git, GitHub, LaboChat | Edycja kodu, kontrola wersji w repozytorium oraz koordynacja zadań w dwuosobowym zespole. |
| **Wsparcie AI** | Gemini (Google) – plan bezpłatny | Generowanie szkieletu aplikacji, zapytań SQL i scenariuszy testowych na podstawie Road Map v1. |

## 2. Uzasadnienie wyboru (5–8 zdań)
Wybraliśmy zestaw oparty na języku Python 3 oraz mikroframeworku Flask, ponieważ pozwala on na bardzo szybkie uruchomienie lokalnego serwera bez skomplikowanej konfiguracji. W dwuosobowym zespole kluczowe było zminimalizowanie narzutu technologicznego, aby skupić się na poprawnym działaniu trzech głównych funkcji MVP (F01–F03). Wbudowany w Pythona moduł `sqlite3` umożliwia przechowywanie danych w jednym pliku lokalnym (`sniezka.db`), co eliminuje konieczność instalacji zewnętrznego serwera bazodanowego. Dzięki zastosowaniu szablonów Jinja2 wszystkie trzy widoki korzystają ze wspólnego układu nawigacji i komunikatów błędów. Takie podejście gwarantuje, że każda osoba z zespołu może uruchomić projekt na swoim komputerze za pomocą trzech prostych poleceń w terminalu. Rozwiązanie jest w pełni darmowe, lekkie i idealnie dopasowane do wymagań pierwszej iteracji v1.
