import geocoder
import requests

destinations = [
    'Space Needle',
    'Crater Lake',
    'Golden Gate Bridge',
    'Yosemite National Park',
    'Las Vegas, Nevada',
    'Grand Canyon National Park',
    'Aspen, Colorado',
    'Mount Rushmore',
    'Yellowstone National Park',
    'Sandpoint, Idaho',
    'Banff National Park',
    'Capilano Suspension Bridge'
]

API_BASE_URL = "https://api.darksky.net/forecast/c73c375afbedccd447f98b4e275bb84c/"

for point in destinations:
    g = geocoder.arcgis(point)
    full_api_url = f'{API_BASE_URL}{g.lat},{g.lng}'
    result = requests.request('GET', full_api_url).json()
    currently = result['currently']['summary']
    temperature = result['currently']['temperature']
    print(f'The {point} is located at ({g.lat}, {g.lng})\nAt {point} right now it is {currently} with a temperature of {temperature}.')