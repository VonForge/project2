from flask import Flask
import sqlite3
def InSert(Nn, time, AirT, AirH, SoilH, Light):
  cursor.execute('INSERT INTO BD_Plant (N, Time, AirTemperature_Ard, AirHumidity_Ard, SoilHumidity_Ard, Ligdt_Ard) VALUES (?, ?, ?, ?, ?, ?)', (Nn, time, AirT, AirH, SoilH, Light))
def SelecT(nameST, n):
  cursor.execute(f'SELECT {nameST} FROM BD_Plant WHERE age > ?', (n,))


connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS BD_Plant (
id INTEGER PRIMARY KEY,
N INTEGER NOT NULL,
Time INTEGER NOT NULL,
AirTemperature_Ard REAL NOT NULL,
AirHumidity_Ard REAL,
SoilHumidity_Ard REAL,
Ligdt_Ard REAL,
)
''')

'''
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 28))
# Обновляем возраст пользователя "newuser"
cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (29, 'newuser'))
cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser',))

# Выбираем всех пользователей
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

# Выводим результаты
for user in users:
  print(user)
'''

'''
# Выбираем имена и возраст пользователей старше 25 лет
cursor.execute('SELECT username, age FROM Users WHERE age > ?', (25,))
results = cursor.fetchall()

for row in results:
  print(row)
'''

connection.commit()
connection.close()
