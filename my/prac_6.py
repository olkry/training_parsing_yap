# Импортируйте все нужные библиотеки.
import requests
from bs4 import BeautifulSoup

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session, declared_attr

PEP_URL = 'https://peps.python.org/numerical/'

# Создайте модель Pep для таблицы pep в декларативном стиле ORM.
# Атрибуты модели:
# 1. id, целочисленное значение, primary key
# 2. type_status, строка с максимальной длиной 2 символа
# 3. number, целочисленное значение, уникальное
# 4. title, строка с максимальной длиной 200 символов
# 5. authors, строка с максимальной длиной 200 символов


class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Pep(Base):
    type_status = Column(String(2))
    number = Column(Integer, unique=True)
    title = Column(String(200))
    authors = Column(String(200))


if __name__ == '__main__':
    engine = create_engine('sqlite:///sqlite.db')
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Ваш код - здесь:
    # создайте таблицу в БД;
    # загрузите страницу PEP_URL;
    # создайте объект BeautifulSoup;
    # спарсите таблицу построчно и запишите данные в БД.

    response = requests.get(PEP_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    table = soup.find('table',
                      attrs={'class': 'pep-zero-table docutils align-default'})
    tbody = table.find('tbody')
    peps = tbody.find_all('tr')
    results = []

    for pep in peps:
        data = pep.text.split('\n')[:-2]
        pep_done = Pep(
            type_status=data[0],
            number=int(data[1]),
            title=data[2],
            authors=data[3]
        )
        results.append(pep_done)

    session.add_all(results)
    session.commit()
