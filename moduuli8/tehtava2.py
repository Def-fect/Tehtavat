import pymysql

yhteys = pymysql.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='deffect',
    password='qwerty',
    autocommit=True,
)

x=input("anna maan koodi")

sql = (f"select type, count(*) "
       f"from airport "
       f"where iso_country in( "
       f"select iso_country from country "
       f"where country.iso_country='{x}')"
       f"group by type;"
       )

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

print(tulos)



