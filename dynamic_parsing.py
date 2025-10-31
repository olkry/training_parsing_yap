from requests_html import HTMLSession
from bs4 import BeautifulSoup


if __name__ == '__main__':
    # Создание сессии, все запросы будут отправляться через неё.
    session = HTMLSession()
    response = session.get('https://httpbin.org/')
    response.html.render(sleep=5)
    soup = BeautifulSoup(response.html.html, 'lxml')
    swagger = soup.find(id='swagger-ui')
    print(swagger.prettify())
