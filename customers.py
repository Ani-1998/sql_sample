import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, surname)"
val = [
  ("Ani", "Mirzoyan"),
  ("Hasmik", "Miqayelyan"),
  ("Narek", "Mnacakanyan"),
  ("Emili", "Qocharyan"),
  ("Grigor", "Mnacakanyan"),
  ("Nare", "Muradyan"),
  ("Erik", "Miqayelyan"),
  ("Sofi", "Margaryan"),
  ("Miqayel", "Sadoyan"),
  ("Anna", "Barsexyan")
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")