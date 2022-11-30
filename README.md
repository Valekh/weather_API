# weather_API
<h1 align="center">Веб-сервис погоды</h1>

Веб-сервис, реализованный с помощью FastAPI. 
Имеет два эндпоинта:
<ul>
<li>GET /weather - текущая погода в Москве (в Цельсиях).
  Пример:</li>
  
```{"temp":-8.32}```
  
<li>GET /history - все среднесуточные температуры из базы данных (выдаёт ошибку при отсутствии записей). Пример успешного выполнения:</li>
</ul>

```{"30.11.2022":{"temp":"-9.84"}}```

<h2 align="center">Подробнее о модулях</h2>
<ul>
<li>
<b>main.py</b> - основной модуль с тремя функциями, где:

<b>get_weather() - </b> выдаёт прогноз погоды, если прошло больше часа с последнего запроса, в противном случае выдаёт результат последнего запроса. Также обновляет среднесуточную температуру на сегодняшний день, обращаясь к функции <b>update_average()</b>

<b>get_history()</b> - отображает среднесуточные температуры. Если записей в базе данных записей об этом нет - выдаёт ошибку.

<b>update_average()</b> - получает результаты всех запросов за сегодняшний день в виде списка, добавляет в него новый, находит среднее значение и записывает в качестве среднесуточной температуры.
Так как OpenWeatherAPI не имеет бесплатных планов для получения истории погоды за какой-либо день, реализовано таким образом.
</li>
<li>
<b>weather_module.py</b> - модуль с единственной функцией <b>current_weather()</b>, получающей актуальную температуру в Москве.
</li>
<li>
<b>sqlite_module.py</b> - модуль для работы с базой данных SQlite. Содержит следующие функции:

<b>create_tables()</b> - создаёт файл .db с двумя таблицами: current_weather и history. Также вписывает в первую дефолтный запрос на 30.11.2022.

<b>sql_put() и sql_get()</b> - две функции для ввода и получения данных из таблиц, созданы для упрощения чтения кода.

<b>get_all_values()</b> - получает все значения из таблицы history в виде словаря (создан для функции <b>update_average() в main.py).</b>

<b>update_average()</b> - обновляет среднесуточную температуру в базе данных, если она есть, или создаёт запись о ней, если её ещё нет.
