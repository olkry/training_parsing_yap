# Допишите необходимые импорты.
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, declared_attr, Session


class Base:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Pep(Base):
    pep_number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(20))

    def __repr__(self):
        return f'PEP {self.pep_number} {self.name}'


if __name__ == '__main__':
    engine = create_engine('sqlite:///sqlite_train.db')
    # Ваш код - здесь.
    '''1.
    При помощи метода session.query() определите в базе данных количество объектов модели Pep, у которых значение поля status равно 'Final'. 
    Напечатайте в консоли полученное число.'''
    session = Session(engine)
    result = session.query(Pep).filter(Pep.status == 'Final').count()
    print(result)

    '''2.
    Подсчитайте количество записей, у которых в поле status указано значение 
    'Final', а значение в поле pep_number меньше 3111.
    Полученное число напечатайте в консоли.
    '''
    session = Session(engine)
    result = session.query(Pep).filter(
        Pep.status == 'Final', Pep.pep_number < 3111
    ).count()
    print(result)

    '''3.
    Удалите из базы все записи со статусом 'Rejected' и 
    подсчитайте количество оставшихся записей.
    Полученное число напечатайте в консоли.
    '''
    session = Session(engine)
    session.query(Pep).filter(Pep.status == 'Rejected').delete()
    session.commit()
    result = session.query(Pep).count()
    print(result)

    '''4.
    Во всех записях, у которых status == 'Active', замените значение 
    поля status на 'Final'. Примените изменения к БД. 
    Подсчитайте общее количество записей со статусом 'Final'. 
    Полученное число напечатайте в консоли.
    '''
    session = Session(engine)
    session.query(Pep).filter(Pep.status == 'Active').update(
        {'status': 'Final'}
    )
    session.commit()
    result = session.query(Pep).filter(Pep.status == 'Final').count()
    print(result)
