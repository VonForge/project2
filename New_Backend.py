from flask import Flask, render_template, jsonify, request
import sqlite3
import socket
import threading
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

def socket_listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 700))  # Здесь настраиваем порт
    s.listen(5)


    while True:
        conn, addr = s.accept()
        data = conn.recv(1024).decode('utf-8')
        if data:
            InSert(data)
        conn.close()

# Запускаем сокет в отдельном потоке
threading.Thread(target=socket_listener, daemon=True).start()

@app.route('/data', methods=['GET'])
def get_data():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data')
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)


app = Flask('_main_')
if '_main_'=='_main_':
    app.run(debug=True, host='0.0.0.0',port=80)








