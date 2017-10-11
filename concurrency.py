from threading import Thread
import json
from urllib.request import urlopen
import time
import os

CITIES = ['New York', 'White plains', 'Dobbs Ferry', 'Hartsdale', 'tarrytown', 'irvington']
APIKEY = os.environ["WEATHER_APIKEY"]

class TempGetter(Thread):
    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        url_template = ('http://api.openweathermap.org/data/2.5/weather?q={},US&appid={}&units=imperial')
        response = urlopen(url_template.format(self.city, APIKEY))
        data = json.loads(response.read().decode())
        self.tempreature = data['main']['temp']

threads = [TempGetter(c) for c in CITIES]

start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

for thread in threads:
   print("it is {0.tempreature:.0f}°F in {0.city}".format(thread))

print("Got {} temps in {} seconds".format(len(threads), time.time() - start))
