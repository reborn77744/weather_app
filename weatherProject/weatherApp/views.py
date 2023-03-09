from django.shortcuts import render
import json
import requests
import environ

env = environ.Env()
environ.Env.read_env()

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'appid': env('appid'), 'units': 'metric'}
        source = requests.get(url, params=params)

        list_of_data = source.json()

        data = {
            "country_code": str(list_of_data["sys"]['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + '℃',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "main": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": list_of_data['weather'][0]['icon'],
        }

    else:
        data = {}

    return render(request, 'weatherApp/index.html', data)



        