from django.shortcuts import render
from urllib2 import Request, urlopen
import json
# Create your views here.


def index(request):
    weather = Request('http://api.openweathermap.org/data/2.5/weather?q=amsterdam,NL&'
                      'mode=json&units=metric&APPID=a9b713dc52746a516bd62818cfd96e4e')
    response = urlopen(weather)
    weather = response.read()
    l = json.loads(weather)

    main = l['main']
    pressure = main['pressure']
    temp_min = main['temp_min']
    temp_max = main['temp_max']
    temp = main['temp']
    humidity = main['humidity']

    clouds = l['clouds']
    allclouds = clouds['all']

    description = l['weather']
    d = description[0]
    description = d['description']

    name = l['name']

    return render(request, 'weather/index.html', {
                                                  'main': main,
                                                  'pressure': pressure,
                                                  'temp_min': temp_min,
                                                  'temp_max': temp_max,
                                                  'temp': temp,
                                                  'humidity': humidity,
                                                  'allclouds': allclouds,
                                                  'description': description,
                                                  'name': name,

                                                  })
