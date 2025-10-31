from sqlalchemy import (
    create_engine, Column, Integer, String, delete
)
from sqlalchemy.orm import declarative_base, Session, declared_attr


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
    engine = create_engine('sqlite:///sqlite.db',
                           echo=False)  # echo вывод в консоль
    # Base.metadata.create_all(engine)

    session = Session(engine)
    ''' Создание и query
        # pep8 = Pep(
        #     pep_number=8,
        #     name='Style Guide for Python Code',
        #     status='Active'
        # )
        # pep20 = Pep(
        #     pep_number=20,
        #     name='The Zen of Python',
        #     status='Active'
        # )
        # pep216 = Pep(
        #     pep_number=216,
        #     name='Docstring Format',
        #     status='Rejected'
        # )

        # session.add(pep8)
        # session.add_all(
        #     (pep20, pep216)
        # )
        # session.commit()

        # results = session.query(Pep).all()
        # print(results)
        # results = session.query(Pep.name, Pep.status).first()
        # print(results)

        # results = session.query(Pep).first()
        # print(results)

        # results = session.query(Pep).filter(Pep.status == 'Active')
        # # Переменная results хранит объект Query...
        # print(type(results))
        # # ...который содержит только те объекты модели Pep, у которых поле status == 'Active'
        # print(results.all()) 
        # # Получить первые два элемента.
        # results = session.query(Pep).limit(2)
        # print(results.all())

        # # Получить все элементы, начиная со второго.
        # results = session.query(Pep).offset(1)
        # print(results.all()) 
        # result = session.query(Pep).all()
        # print(type(result))

        # result = session.query(Pep)
        # print(type(result))

        # result = session.query(Pep).filter(Pep.status == 'Active').first()
        # print(type(result))

        # result = session.query(Pep.name).filter(Pep.status == 'Active')
        # print(type(result))

        # result = session.query(Pep).limit(2)
        # print(type(result))

        # result = session.query(Pep).filter(Pep.status == 'Active').all()
        # print(type(result))

        # # Получаем объект из базы:
        # pep8 = session.query(Pep).filter(Pep.pep_number == '8').first()
        # # Заменяем свойство объекта:
        # pep8.status = 'Closed'
        # # Коммитим:
        # session.commit()

        # # Вызываем метод update() объекта Query, 
        # # который хранит все объекты модели PEP:
        # session.query(Pep).update(
        #     {'status': 'Active'}
        # )

        # session.commit()

        # pep8 = session.query(Pep).filter(Pep.pep_number == '8').first()
        # session.delete(pep8)
        # session.commit()

        # session.query(Pep).filter(Pep.pep_number > 20).delete()
        # session.commit()
    '''

    # session.execute(
    #     insert(Pep).values(
    #         pep_number='1000',
    #         name='Pep from Future',
    #         status='Proposal'
    #     )
    # )
    # session.commit()

    # result = session.execute(
    #     select(Pep).where(Pep.status == 'Active')
    # )
    # # print(type(result))
    # # print(result)
    # # print(type(result.all()))
    # print(result.all())

    # session.execute(
    #     update(Pep).where(Pep.pep_number == 1000).values(status='Active')
    # )
    # session.commit() 

    session.execute(
        delete(Pep).where(Pep.status == 'Active')
    )
    session.commit()



