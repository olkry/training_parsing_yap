import requests_cache
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm

WHATS_NEW_URL = 'https://docs.python.org/3/whatsnew/'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(WHATS_NEW_URL)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, features='lxml')
    # Шаг 1-й: поиск в "супе" тега section с нужным id. Парсеру нужен только
    # первый элемент, поэтому используется метод find().
    main_div = soup.find('section', attrs={'id': 'what-s-new-in-python'})
    # Шаг 2-й: поиск внутри main_div
    # следующего тега div с классом toctree-wrapper.
    # Здесь тоже нужен только первый элемент, используется метод find().
    div_with_ul = main_div.find('div', attrs={'class': 'toctree-wrapper'})
    # Шаг 3-й: поиск внутри div_with_ul
    # всех элементов списка li с классом toctree-l1.
    # Нужны все теги, поэтому используется метод find_all().
    sections_by_python = div_with_ul.find_all('li',
                                              attrs={'class': 'toctree-l1'})
    results = []
    # Печать первого найденного элемента.
    for section in tqdm(sections_by_python):
        version_a_tag = section.find('a')
        href = version_a_tag['href']
        version_link = urljoin(WHATS_NEW_URL, href)

        # Здесь начинается новый код!
        response = session.get(version_link)  # Загрузите все страницы со
        # статьями. Используйте кеширующую сессию.
        response.encoding = 'utf-8'  # Укажите кодировку utf-8.
        soup = BeautifulSoup(response.text, features='lxml')  # Сварите супчик.
        h1 = soup.find('h1')  # Найдите в "супе" тег h1.
        dl = soup.find('dl')  # Найдите в "супе" тег dl.
        dl_text = dl.text.replace('\n', ' ')

        # Добавьте в вывод на печать текст из тегов h1 и dl.
        # print(version_link, h1.text, dl_text)

        # Добавьте в список ссылки и текст из тегов h1 и dl в виде кортежа.
        results.append(
            (version_link, h1.text, dl_text)
        )

    # Печать списка с данными.
    for row in results:
        # Распаковка каждого кортежа при печати при помощи звездочки.
        print(*row)
