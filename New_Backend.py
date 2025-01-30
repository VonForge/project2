from flask import Flask
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
