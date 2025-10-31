from prettytable import PrettyTable

if __name__ == '__main__':
    yp_table = PrettyTable()
    yp_table.field_names = (
        '№ когорты',
        'Кол-во студентов',
        'Средний балл',
    )
    yp_table.add_row([16, 200, 4.5])  # Списком
    yp_table.add_row((17, 155, 4.7))  # Котрежем
    yp_table.add_rows(((18, 211, 4.3), (19, 300, 5),))

    print(yp_table)
