from flask import Flask
from socket import *
import sqlite3
def InSert(Nn, Time, AirT, AirH, SoilH, Light):
  cursor.execute('INSERT INTO BD_Plant (N, Time, AirTemperature_Ard, AirHumidity_Ard, SoilHumidity_Ard, Ligdt_Ard) VALUES (?, ?, ?, ?, ?, ?)', (Nn, Time, AirT, AirH, SoilH, Light))
def SelecT(Num):
  cursor.execute(f'SELECT Text FROM BD_text WHERE id = ?', (Num,))
  DANN = cursor.fetchall()
  return DANN

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS BD_text (
id INTEGER PRIMARY KEY,
N INTEGER NOT NULL,
Text TEXT NOT NULL,
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS BD_Plant (
id INTEGER PRIMARY KEY,
N INTEGER NOT NULL,
Time INTEGER NOT NULL,
AirTemperature_Ard REAL NOT NULL,
AirHumidity_Ard REAL NOT NULL,
SoilHumidity_Ard REAL NOT NULL,
Ligdt_Ard REAL NOT NULL,
)
''')

connection.commit()
connection.close()

con = sqlite3.connect('BD_Plant')
cur = con.cursor()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("", 700))

sock.listen(1)


app = Flask('MMS')
if 'MMS'=='_main_':
    app.run(debug=True)


while True:
    conn, addr = sock.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print('Received data:', data.decode())
    conn.close()
    break

sock.close()
con.close()




