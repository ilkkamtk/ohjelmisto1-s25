import mysql.connector
from flask import Flask

yhteys = mysql.connector.connect(
    host="mysql.metropolia.fi",
    port=3306,
    database="ilkkamtk",
    user="ilkkamtk",
    password="q1w2e3r4",
    autocommit=True
)

def haeLentokentta(koodi):
    sql = f"SELECT * FROM airport WHERE ident=%s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (koodi,))
    return kursori.fetchone()

app = Flask(__name__)

@app.route('/airport/<icao>')
def get_airport(icao):
    return haeLentokentta(icao)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)