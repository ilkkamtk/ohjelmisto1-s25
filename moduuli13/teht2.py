import mysql.connector
from flask import Flask
from flask_cors import CORS

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
    tulos = kursori.fetchone()
    print('Debug', tulos)
    return tulos

app = Flask(__name__)
cors = CORS(app)

@app.route('/airport/<icao>')
def get_airport(icao):
    try:
        lentokentta = haeLentokentta(icao)
        if lentokentta is None:
            return {"error": "Lentokenttää ei löydy"}, 404
        return lentokentta
    except mysql.connector.errors.ProgrammingError as err:
        print(err)
        return {"error": "räätälöity virheilmoitus"}, 500
    except Exception as err:
        print(err)
        return {"error": "geneerinen virheilmoitus"}, 500


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)