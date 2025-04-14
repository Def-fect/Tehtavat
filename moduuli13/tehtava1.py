from flask import Flask, Response, request
import json

app = Flask(__name__)


@app.route('/alkuluku/<luku2>')
def tarkista_alkuluku(luku2):
    luku1 = float(luku2)
    try:
        if luku1 > 1:
            for i in range(2, int(luku1 ** 0.5) + 1):
                if luku1 % i == 0:
                    tulos = f"{luku1} ei ole alkuluku"
                    break
            else:
                tulos = f"{luku1} on alkuluku"
        else:
            tulos = f"{luku1} ei ole alkuluku"

        vastaus = {
            "status": 200,
            "tulos": tulos,
            "luku": luku1
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
