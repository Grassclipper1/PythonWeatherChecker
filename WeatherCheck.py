import requests
from CityFinder import find_city
from WeatherSymbol import find_weather

# link to SMHI:s api
url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/" \
      "geotype/point/lon/{lon}/lat/{lat}/data.json"


def check_weather(city):
    lat, lng = None, None
    # look up the latitude and longitude of a city
    try:
        lat, lng = find_city(city)
    except TypeError:
        pass

    # return standard message if city does not exist in database/dict
    if lat is None or lng is None:
        return "City not in database", "", f'images/nocity.png'

    # gets the link to SMHI:s API and puts in the coordinates of the city that you entered
    response = requests.get(url.format(lon=lng, lat=lat))

    # get json data and extract the temperature and weather from it
    data = response.json()
    temperature = data['timeSeries'][0]['parameters'][10]['values'][0]
    wysmb2 = data['timeSeries'][0]['parameters'][-1]['values'][0]
    kind_of_weather = find_weather(wysmb2).lower()
    # gets the image corresponding to the type of weather
    image = get_image(wysmb2)

    return f"The temperature in {city} is {temperature}\N{DEGREE SIGN}C", \
        f"It is {kind_of_weather}", f'images/{image}'


def get_image(n):
    if n in [1, 2]:
        return "sunny.png"
    elif n in [3, 4, 5, 6, 7]:
        return "cloudy.png"
    elif n in [8, 9, 10, 11, 18, 19, 20, 21]:
        return "rain.png"
    elif n in [12, 13, 14, 15, 16, 17, 22, 23, 24, 25, 26, 27]:
        return "snow.png"
    else:
        return "nocity.png"
