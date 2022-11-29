from datetime import datetime
from statistics import mean

from fastapi import FastAPI, HTTPException

import weather_module
import sqlite_module

app = FastAPI()


@app.get("/weather")
def get_weather():
    now = datetime.now()
    last_temp = sqlite_module.get_last_temp()
    last_time = datetime.strptime(last_temp[2], "%H:%M")

    if (now - last_time).seconds >= 3600:
        temp = weather_module.current_weather()
        current_date = now.strftime("%d.%m.%Y")
        current_time = now.strftime("%H:%M")
        sqlite_module.put_temp(current_date, current_time, temp)
        update_average(current_date, temp)
    else:
        temp = last_temp[3]
    return {'temp': temp}


@app.get("/history")
def get_history():
    averages = sqlite_module.get_history()
    averages_temp = {}
    for i in averages:
        averages_temp.update({i[0]: {'temp': i[1]}})

    if len(averages) == 0:
        raise HTTPException(status_code=404, detail="No history")
    else:
        return averages_temp


def update_average(date: str, new_value: str):
    dates = sqlite_module.get_all_values(date)
    dates = list(map(float, dates))
    dates.append(new_value)
    average = round(mean(dates), 2)
    sqlite_module.update_average(date, str(average))


sqlite_module.create_tables()

