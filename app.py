import sqlite3
import uuid
from datetime import date
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "sniezka-sekretny-klucz-v1"
DB_NAME = "sniezka.db"
DEMO_USER_ID = 1


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS uzytkownik (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                imie TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS oferta (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nazwa TEXT NOT NULL,
                cena REAL NOT NULL,
                opis TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS karnet (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                uzytkownik_id INTEGER NOT NULL,
                oferta_id INTEGER NOT NULL,
                data_waznosci TEXT NOT NULL,
                kod_qr TEXT NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (uzytkownik_id) REFERENCES uzytkownik(id),
                FOREIGN KEY (oferta_id) REFERENCES oferta(id)
            )
        """)

        user_exists = conn.execute(
            "SELECT id FROM uzytkownik WHERE id = ?", (DEMO_USER_ID,)
        ).fetchone()
        if not user_exists:
            conn.execute(
                "INSERT INTO uzytkownik (id, imie, email) VALUES (?, ?, ?)",
                (DEMO_USER_ID, "Jan Nowak", "jan.nowak@example.com"),
            )

        offers_count = conn.execute("SELECT COUNT(*) AS cnt FROM oferta").fetchone()["cnt"]
        if offers_count == 0:
            oferty_startowe = [
                ("Karnet Dorosły (Normalny)", 79.00, "Całodzienny dostęp do wszystkich wyciągów stacji Śnieżka."),
                ("Karnet Student (Ulgowy)", 59.00, "Zniżka dla uczniów i studentów za okazaniem ważnej legitymacji."),
                ("Karnet Dziecko", 39.00, "Całodzienny karnet dla dzieci do 12 roku życia."),
            ]
            conn.executemany(
                "INSERT INTO oferta (nazwa, cena, opis) VALUES (?, ?, ?)",
                oferty_startowe,
            )
    conn.close()


@app.cli.command("init-db")
def init_db_command():
    """Inicjalizuje bazę danych SQLite i dodaje dane startowe."""
    init_db()
    print("Baza danych sniezka.db została zainicjalizowana pomyślnie.")


# Automatyczna inicjalizacja przy starcie, jeśli plik bazy jeszcze nie istnieje
init_db()


@app.route("/")
def w01_oferta():
    conn = get_db()
    oferty = conn.execute("SELECT id, nazwa, cena, opis FROM oferta ORDER BY id").fetchall()
    user = conn.execute("SELECT imie, email FROM uzytkownik WHERE id = ?", (DEMO_USER_ID,)).fetchone()
    conn.close()
    return render_template("layout.html", view="W01", oferty=oferty, user=user)


@app.route("/kup", methods=["GET", "POST"])
def w02_kup():
    conn = get_db()
    oferty = conn.execute("SELECT id, nazwa, cena, opis FROM oferta ORDER BY id").fetchall()
    user = conn.execute("SELECT imie, email FROM uzytkownik WHERE id = ?", (DEMO_USER_ID,)).fetchone()
    wybrana_oferta_id = request.args.get("oferta_id", type=int)

    if request.method == "POST":
        oferta_id = request.form.get("oferta_id", type=int)
        data_waznosci = request.form.get("data_waznosci", "").strip()

        if not oferta_id or not data_waznosci:
            flash("Błąd: Wszystkie pola są wymagane. Wybierz rodzaj karnetu i datę ważności.", "error")
            conn.close()
            return render_template(
                "layout.html", view="W02", oferty=oferty, user=user, wybrana_oferta_id=oferta_id
            )

        try:
            wybrana_data = date.fromisoformat(data_waznosci)
        except ValueError:
            flash("Błąd: Niepoprawny format daty (oczekiwano RRRR-MM-DD).", "error")
            conn.close()
            return render_template(
                "layout.html", view="W02", oferty=oferty, user=user, wybrana_oferta_id=oferta_id
            )

        if wybrana_data < date.today():
            flash("Błąd: Data ważności karnetu nie może być z przeszłości.", "error")
            conn.close()
            return render_template(
                "layout.html", view="W02", oferty=oferty, user=user, wybrana_oferta_id=oferta_id
            )

        kolizja = conn.execute(
            """
            SELECT id FROM karnet
            WHERE uzytkownik_id = ? AND oferta_id = ? AND data_waznosci = ? AND status = 'Aktywny'
            """,
            (DEMO_USER_ID, oferta_id, data_waznosci),
        ).fetchone()

        if kolizja:
            flash(
                "Błąd: Posiadasz już aktywny karnet tego samego typu na wybrany dzień. Wybierz inną datę lub anuluj obecny karnet.",
                "error",
            )
            conn.close()
            return render_template(
                "layout.html", view="W02", oferty=oferty, user=user, wybrana_oferta_id=oferta_id
            )

        kod_qr = f"QR-{uuid.uuid4().hex[:6].upper()}"
        with conn:
            conn.execute(
                """
                INSERT INTO karnet (uzytkownik_id, oferta_id, data_waznosci, kod_qr, status)
                VALUES (?, ?, ?, ?, 'Aktywny')
                """,
                (DEMO_USER_ID, oferta_id, data_waznosci, kod_qr),
            )
        conn.close()
        flash(f"Karnet został pomyślnie zarezerwowany! Wygenerowano kod: {kod_qr}", "success")
        return redirect(url_for("w03_moje_karnety"))

    conn.close()
    return render_template(
        "layout.html", view="W02", oferty=oferty, user=user, wybrana_oferta_id=wybrana_oferta_id
    )


@app.route("/moje-karnety")
def w03_moje_karnety():
    conn = get_db()
    user = conn.execute("SELECT imie, email FROM uzytkownik WHERE id = ?", (DEMO_USER_ID,)).fetchone()
    karnety = conn.execute(
        """
        SELECT k.id, k.data_waznosci, k.kod_qr, k.status, o.nazwa AS oferta_nazwa, o.cena
        FROM karnet k
        JOIN oferta o ON k.oferta_id = o.id
        WHERE k.uzytkownik_id = ?
        ORDER BY k.id DESC
        """,
        (DEMO_USER_ID,),
    ).fetchall()
    conn.close()
    return render_template("layout.html", view="W03", karnety=karnety, user=user)


@app.route("/anuluj/<int:karnet_id>", methods=["POST"])
def anuluj_karnet(karnet_id):
    conn = get_db()
    karnet = conn.execute(
        "SELECT id, status FROM karnet WHERE id = ? AND uzytkownik_id = ?",
        (karnet_id, DEMO_USER_ID),
    ).fetchone()

    if not karnet:
        flash("Błąd: Nie znaleziono wskazanego karnetu przypisanego do Twojego konta.", "error")
    elif karnet["status"] != "Aktywny":
        flash("Błąd: Ten karnet został już wcześniej anulowany.", "error")
    else:
        with conn:
            conn.execute(
                "UPDATE karnet SET status = 'Anulowany' WHERE id = ? AND uzytkownik_id = ?",
                (karnet_id, DEMO_USER_ID),
            )
        flash("Karnet został pomyślnie anulowany. Termin został zwolniony.", "success")

    conn.close()
    return redirect(url_for("w03_moje_karnety"))


if __name__ == "__main__":
    app.run(debug=True)
