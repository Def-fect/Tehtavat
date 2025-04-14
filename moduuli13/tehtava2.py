from flask import Flask, Response, request
import json, pymysql

yhteys = pymysql.connect(
    host='localhost',
    port=3306,
    database='airplane_simulator_v3',
    user='user',
    password='password',
    autocommit=True,
)
app = Flask(__name__)


@app.route('/kenttä/<icao>')
def tarkista_alkuluku(icao):

    try:
        sql = (f"select  ident, name, municipality "
               f"from airport "
               f"where ident='{icao}';"
               )
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchone()

        vastaus = {
            "ICAO": tulos[0],
            "Name": tulos[1],
            "Municipality": tulos[2]
        }
        tilakoodi = 200

    except Exception as e:
        vastaus = {
            "status": 400,
            "virhe": str(e)
        }
        tilakoodi = 400

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(virhekoodi):
    print(virhekoodi)
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
