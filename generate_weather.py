import csv
import math
import os
import sys

from collections import namedtuple
from datetime import datetime, timedelta
from random import randint, random, normalvariate
from multiprocessing import Pool
from contextlib import closing
from weather_models import WEATHER_MODELS

from constants import INPUT_CITIES, NUM_DAYS, CONDITIONS_LIST, val

City = namedtuple('City', ['IATA', 'latitude', 'longitude', 'altitude'])


# Global airport database information downloaded from
# http://www.partow.net/miscellaneous/airportdatabase/index.html#Downloads
# Take an IATA code as input, and return a City as output
# The city data is read from the `GlobalAirportDatabase.txt` file
def to_city(IATA):
    with open('./GlobalAirportDatabase.txt') as fin:
        cities_reader = csv.reader(fin, delimiter=':')
        for row in cities_reader:
            if row[1] == IATA:
                return City(row[1],
                            float(row[14]),
                            float(row[15]),
                            math.trunc(float(row[13])))


# Generate a list of `num` random datetimes starting from start_date
def generate_dates(IATA, start_date=datetime(2007,1,1, 0, 0, 0), num=NUM_DAYS):
    return [start_date + timedelta(days=i, hours=randint(0,23), minutes=randint(0,60), seconds=randint(0,60))
            for i in range(num)]


def generate_conditions(IATA, num=NUM_DAYS):
    return [weighted_choice(CONDITIONS_LIST, WEATHER_MODELS[IATA].condition_weights)[0] for i in range(num)]


def generate_temperature(IATA, month, condition):
    model = WEATHER_MODELS[IATA]
    return normalvariate(model.temperature[month].mean, model.temperature[month].var) + model.temperature[month].adjust[val(condition)]


def generate_pressure(IATA, month, condition):
    model = WEATHER_MODELS[IATA]
    return normalvariate(model.pressure[month].mean, model.pressure[month].var) + model.pressure[month].adjust[val(condition)]


def generate_humidity(IATA, month, condition):
    model = WEATHER_MODELS[IATA]
    return normalvariate(model.humidity[month].mean, model.humidity[month].var) + model.humidity[month].adjust[val(condition)]


def weighted_choice(seq, weights):
    assert len(weights) == len(seq)
    assert (abs(1.0 - sum(weights)) < 1e-6)
    x = random()
    for i, _ in enumerate(seq):
        if x <= weights[i]:
            return seq[i]
        x -= weights[i]


def generate_weather(IATA, num=NUM_DAYS):
    city = to_city(IATA)
    dates = generate_dates(IATA)
    conditions = generate_conditions(IATA)

    with open('./tmp/{0}'.format(IATA), 'w') as fout:
        for i in range(num):
            temperature = generate_temperature(IATA, dates[i].month-1, conditions[i])
            pressure = generate_pressure(IATA, dates[i].month-1, conditions[i])
            humidity = generate_humidity(IATA, dates[i].month-1, conditions[i])
            fout.write('{}|{},{},{}|{}|{}|{:+2.1f}|{:4.1f}|{:2.0f}\n'.format(
                city.IATA,
                city.latitude,
                city.longitude,
                city.altitude,
                dates[i].strftime("%Y-%m-%dT%H:%M:%SZ"),
                conditions[i],
                temperature,
                pressure,
                humidity
            ))


if __name__ == '__main__':
    with closing(Pool(processes=4)) as pool:
        pool.map(generate_weather, list(INPUT_CITIES))
        pool.terminate()

    for _, _, files in os.walk('./tmp'):
        for filename in files:
            with open('./tmp/{0}'.format(filename)) as fin:
                for line in fin:
                    sys.stdout.write(line)