import requests_cache

from ans import API_KEY

TIME_API_URL = 'http://api.weatherapi.com/v1/'
API_KEY = API_KEY
LOC = 'Moscow'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    # moscow_url = TIME_API_URL + f'current.json?key={API_KEY}&q={LOC}'
    timezone_url = TIME_API_URL + f'timezone.json?key={API_KEY}&q={LOC}'
    # response_time = session.get(moscow_url)
    response_zone = session.get(timezone_url)
    # data_time = response_time.json()
    # result_time = data_time.get('location').get('localtime')
    data_zone = response_zone.json().get('location')
    data_time = data_zone.get('localtime')
    print(data_time)
