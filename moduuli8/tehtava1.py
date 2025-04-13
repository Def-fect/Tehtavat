import pymysql

yhteys = pymysql.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='deffect',
    password='qwerty',
    autocommit=True,
)
x=input("Anna koodi")

sql = (f"select country.name, airport.name "
       f"from airport, country "
       f"where airport.iso_country=country.iso_country and airport.ident='{x}';"
)

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

print(tulos)
