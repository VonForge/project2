from flask import *
inport sqlite3
app = Flask(__name__)
@app.route('/')
def Privetstvie():
  return 'Добро пожаловать'
@app.route('/login')
def login():
  pass



<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charaset="UTF-8">
  <title>Сайт системы "SisteMon"
  </title>
</head>
<body>
  <header class="site-header">
    <h1>Сайт системы "SisteMon"
    </h1>
    <img src="Этот комьютер/Изображения/Plant_project_imj_001" alt="" widht='400' height='500'> #если что src изменим
  </header>
    <o>
      <button type='button' name ='Vive_Monsis'>
          <svg wight='60' height='20'>
          </svg>
        Посмотреть устройства
      </button> 
    </o>

    <p>
    </p>
    <select class='Spisok'>
      <option value='GeneralCondition'>{condition_plant_new}</option>
      <option value='DeviceNumber'>{Number_device}</option>
    </select>
  <footer>
    <p>Справочная информация
    </p>
  </footer>
</body>
</html>


