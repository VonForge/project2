from flask import Flask
from flask import render_template
app = Flask(name)

@app.route('/')
def hello_world():
  return 'Hello, World!'

if name == 'main':
  app.run(debug=True)
#
python app.py
#
@app.route('/about')
def about():
  return 'This is the about page'
#
app = Flask(name)

@app.route('/hello/<name>')
def hello(name):
  return render_template('hello.html', name=name)

if name == 'main':
  app.run(debug=True)
#

































