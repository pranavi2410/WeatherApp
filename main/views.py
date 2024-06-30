from django.shortcuts import render 
import json 
import urllib.request 
from urllib.parse import quote

def index(request): 
    if request.method == 'POST': 
        city = request.POST['city']
        api_key = '0ecba1c23a6210f391c76d30da0637d1'  # Replace with your actual API key

        # URL encode the city name
        city_encoded = quote(city)

        # Construct the API URL without spaces
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid={api_key}'

        try:
            # Fetch data from the API
            source = urllib.request.urlopen(url).read()

            # Convert JSON data to a dictionary
            list_of_data = json.loads(source)

            # Extract necessary data
            data = { 
                "country_code": str(list_of_data['sys']['country']), 
                "coordinate": f"{list_of_data['coord']['lon']} lon" + ' '
                              + f"{list_of_data['coord']['lat']} lan", 
                "temp": "{:.2f}°C".format(list_of_data['main']['temp'] - 273.15),
                "pressure": f"{list_of_data['main']['pressure'] / 100000} bar",
                "humidity": f"{list_of_data['main']['humidity']}%",
            } 
            print(data)
        except Exception as e:
            print(f"Error fetching data: {e}")
            data = {}  # Handle error gracefully

    else: 
        data = {} 

    return render(request, "main/index.html", data)

