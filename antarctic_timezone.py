from time import sleep

# Импортируйте библиотеку requests_cache.
import requests_cache
from ans import API_KEY

# TIME_API_URL = 'http://worldtimeapi.org/api/'
TIME_API_URL = 'http://api.weatherapi.com/v1/'
API_KEY = API_KEY
LOC = 'Vostok'


if __name__ == '__main__':
    # Создайте сессию, кеширующую результаты загрузки страниц.
    session = requests_cache.CachedSession()
    # Уточнение местоположения.
    vostok_url = TIME_API_URL + f'timezone.json?key={API_KEY}&q={LOC}'
    # Загружаем текущее время станции "Восток" пять раз. 
    for iteration in range(5):
        # После третьей загрузки — очистка кеша.
        if iteration > 2:
            # Очистите кеш.
            session.cache.clear()
        # Загрузите веб-страницу из переменной vostok_url,
        # используя созданную сессию.
        response = session.get(vostok_url)
        # Ответ от сервера приходит в формате JSON, 
        # поэтому нужно преобразовать его методом .json(), 
        # чтобы дальше работа велась с данными, как со словарём.
        data = response.json().get('location')
        # Получение текущего времени на станции "Восток".
        result = data.get('localtime')
        # Печать номера итерации и текущего времени.
        print(iteration, result)
        # Пауза на одну секуду.
        sleep(1)
    # Получение часового пояса. 
    utc_offset = data.get('tz_id')
    # Печать часового пояса.
    print('Часовой пояс города «Восток»:', utc_offset) 