import requests 

def get_weather_desc_temp():
    api_key = "3ade91b917b2d65627e474b2c10d1a61"
    city = "Eagle Mountain"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max}
def main():
#Print the results
    weather_dict = get_weather_desc_temp()      
    print("Today's forecast is", weather_dict.get('description'))
    print("The minimus temperature is", weather_dict.get('temp_min'))
    print("The maximum temperature is", weather_dict.get('temp_max'))

main()