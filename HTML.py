<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charaset="UTF-8">
  <title>Сайт системы "SisteMon"
  </title>
  <link rel='stylesheet' href='style.css'>
</head>
<body>
  <header class="site-header">
    <h1>Сайт системы "SisteMon"</h1>
    <img src="Этот комьютер/Изображения/Plant_project_img_001" alt="" widht='40' height='40'> #если что src изменим
    <section class='BasicTools'>
      <h3>секции, как вернутся на начальную страницу,
        помотреть оповещения</h3>
    </section>
  </header>
    <o>
      <Pass-Log method='POST'>
        <div class='conteiner'>
          <label for='login'> <a> Login </a> </label>
          <input type='text'>
          <label for='PassworD'> <a> Password </a> </label>
          <input type='password' name='Password'>
          <button type='button' name ='Insert'><svg wight='50' height='30'></svg></button>
        </div>
      </Pass-Log>
      <button type='button' name ='Vive_Monsis'>
          <svg wight='40' height='20'>
          </svg>
        Посмотреть подключённые устройства
      </button>
    </o>
    <p>
    </p>
    <select class='List'>
      <option value='GeneralCondition'>{condition_plant_new}</option>
      <option value='DeviceNumber'>{Number_device}</option>
    </select>
  <footer>
    <p>Справочная информация
    </p>
  </footer>
</body>
</html>
