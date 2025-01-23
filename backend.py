from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask('MMS')

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newflask.db'
db= SQLAlchemy(app)

#ТАБЛИЦА
class Post(db.Model):
    Temperature  = db.Collum(db.Text, primary_key=True)
    Humidity  = db.Collum(db.Text, primary_key=True)
    light = db.Collum(db.Text, primary_key=True)
    Humidity2 = db.Collum(db.Text, primary_key=True)


#шаблончики
@app.route('/main')
@app.route('/')
def m():
    return('')

@app.route('/acc')
def a():
    return('')

@app.route('/main1')
def m():
    return('')

#автоперезапуск
if 'MMS'=='_main_':
    app.run(debug=True)
