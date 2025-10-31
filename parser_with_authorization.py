import requests

from bs4 import BeautifulSoup

LOGIN_URL = 'http://158.160.172.156/login/'

if __name__ == '__main__':
    session = requests.session()
    response = session.get(LOGIN_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    csrf_string = soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})
    token = csrf_string['value']
    
    data = {
        'username': 'test_parser_user',
        'password': 'testpassword',
        'csrfmiddlewaretoken': token
    }

    response = session.post(LOGIN_URL, data=data)
    response.encoding = 'utf-8'
    print(response.text)
