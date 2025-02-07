import pymysql




yhteys = pymysql.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='deffect',
    password='qwerty',
    autocommit=True,

)


sql = (f"SELECT * from airport limit 10")
print(sql)
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

print(tulos)
#Process finished with exit code -1073741819 (0xC0000005)
#Process finished with exit code -1073741819 (0xC0000005)