#У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах за произвольный период по странам
# (структура данных в примере).
# Необходимо написать код, который рассчитает среднюю температуру за период в Цельсиях(!) для каждой страны.

import numpy as np


countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]


def convert_temperatures(temp_f):
    temp = np.array(temp_f)
    temp_c = (temp - 32) / 1.8
    return temp_c

def get_temperatures(temp):
    for i in range(len(countries_temperature)):
        ti = countries_temperature[i][1]
        ti_c = convert_temperatures(ti)
        ti_c_mean = np.round(np.mean(ti_c), 1)
        countries_temperature[i].append(np.mean(ti_c_mean))


get_temperatures(countries_temperature)
print("Средняя температура в странах:")
for i in range(len(countries_temperature)):
    print(countries_temperature[i][0], '-', countries_temperature[i][2])