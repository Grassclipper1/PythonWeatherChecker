import json

# loads all the cities from city_data, encoding makes sure it works with ÅÄÖ
with open('city_data.json', encoding='utf-8') as f:
    data = json.load(f)


def find_city(city_name):
    for city in data:
        if city['city'] == city_name:
            return city['lat'], city['lng']
    return None
