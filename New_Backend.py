from flask import Flask
import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
''')
cursor.execute('CREATE INDEX idx_email ON Users (email)')
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
# Выбираем имена и возраст пользователей старше 25 лет
cursor.execute('SELECT username, age FROM Users WHERE age > ?', (25,))
results = cursor.fetchall()

for row in results:
  print(row)


connection.commit()
connection.close()
