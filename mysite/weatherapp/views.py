import urllib.request
import json
from django.shortcuts import render
# Create your views here.


# def index(request):
#     if request.method == 'POST':
#         city = request.POST['city']
#         source =  urllib.request.urlopen('http://api-openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=d00b54acc2909f876bea1717d8e1fbab').read()
#         data_list = json.loads(source)
#         #  create data dictionary
#         data = {"country_code": str(data_list['sys']['country']),
#                  "coordinates" : str(data_list['coord']['lon']) + str(data_list['coord']['lat']),
#                  "temp" : str(data_list['main']['temp'] + ' C'),
#                  "pressure" : str(data_list['main']['pressure']),
#                  "humidity" : str(data_list['main']['humidity']),
#                  "main" : str(data_list['weather']['main']),
#                  "description" : str(data_list['weather'][0]['description']),
#                  "icon": str(data_list['weather'][0]['icon'])
#                 }
#         print(data)
#     else:
#         data = {}
#     return render(request, "main/index.html", data)


def index(request):

    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api-openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=d00b54acc2909f876bea1717d8e1fbab').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)