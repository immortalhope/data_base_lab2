"""
Толстуха Надія, КМ-82
Варіант 11:
Порівняти середній бал з Фізики у кожному регіоні у 2020 та 2019 роках серед тих
кому було зараховано тест
"""

import psycopg2
import psycopg2.errorcodes
import csv
import datetime
import itertools
import config


# підключення до бази даних
params = config.config()

# connect to the PostgreSQL server
print('Connecting to the PostgreSQL database...')
conn = psycopg2.connect(**params)

cursor = conn.cursor()
# якщо таблиця існує - її необхідно видалити
cursor.execute('DROP TABLE IF EXISTS tbl_open_data_zno;')
conn.commit()


def create_table():
    """
    Функція для створення таблиці з даними
    :return: header
    """
    with open("Odata2019File.csv", "r", encoding="cp1251") as csv_file:
        # список назв усіх колонок
        header = csv_file.readline().split(';')
        header = [word.strip('"') for word in header]
        header[-1] = header[-1].rstrip('"\n')
        # запит для створення колонок для таблиці
        clm_names = "\n\tYear INT,"
        for elm in header:
            if elm == 'OUTID':
                clm_names += '\n\t' + elm + ' VARCHAR(40),'
            elif elm == 'Birth':
                clm_names += '\n\t' + elm + ' INT,'
            elif 'Ball' in elm:
                clm_names += '\n\t' + elm + ' INT,'
            else:
                clm_names += '\n\t' + elm + ' VARCHAR(255),'
        query = '''CREATE TABLE IF NOT EXISTS tbl_open_data_zno(''' + clm_names.rstrip(',') + \
                '\n, PRIMARY KEY(OUTID)\n)'
        cursor.execute(query)
        conn.commit()
        return header


header = create_table()


def insert_data(year, f, conn, cursor, time_f):
    start_time = datetime.datetime.now()
    time_f.write(str(start_time) + " - початок роботи з файлом: " + f + '\n')

    with open(f, "r", encoding="cp1251") as csv_file:
        print("Читається файл " + f)
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        b_size = 100
        b_count = 0
        inserted_all = False
        while not inserted_all:
            try:
                insert_query = '''INSERT INTO tbl_open_data_zno (year, ''' + ', '.join(header) + ') VALUES '
                count = 0
                for row in csv_reader:
                    count += 1
                    # Нормування даних для уникнення помилок
                    for key in row:
                        if row[key] == 'null':
                            pass
                        elif key.lower() != 'birth' and 'ball' not in key.lower():
                            row[key] = "'" + row[key].replace("'", "''") + "'"
                        elif 'ball100' in key.lower():
                            row[key] = row[key].replace(',', '.')
                    insert_query += '\n\t(' + str(year) + ', ' + ','.join(row.values()) + '),'
                    # Якщо набралося 100 рядків - коммітимо транзакцію
                    if count == b_size:
                        b_count += 1
                        count = 0
                        insert_query = insert_query.rstrip(',') + ';'
                        cursor.execute(insert_query)
                        conn.commit()
                        insert_query = '''INSERT INTO tbl_open_data_zno (year, ''' + ', '.join(header) + ') VALUES '
                    # При досягненні 10-ї порції файлу - закриваємо з'єднання, для того щоб протестувати відновлення бд
                    if b_count == 10:
                        conn.close()

                # Якщо досягли кінця файлу - коммітимо транзакцію
                if count != 0:
                    insert_query = insert_query.rstrip(',') + ';'
                    cursor.execute(insert_query)
                    conn.commit()
                inserted_all = True
            except psycopg2.InterfaceError as e:
                # якщо з'єднання з базою даних втрачено
                print("Упс... База даних впала, очікуємо відновлення роботи...")
                time_f.write(str(datetime.datetime.now()) + " - втрата з'єднання з базою даних\n")
                connection = False
                while not connection:
                    try:
                        # намагаємось підключитись до бази даних
                        conn = psycopg2.connect(**params)
                        cursor = conn.cursor()
                        time_f.write(str(datetime.datetime.now()) + " - відновлення з'єднання з базою даних\n")
                        connection = True
                    except psycopg2.OperationalError as e:
                        pass

                print("Ура! З'єднання відновлено, продовжуємо роботу.")
                csv_file.seek(0, 0)
                csv_reader = itertools.islice(csv.DictReader(csv_file, delimiter=';'),
                                              b_count * b_size, None)
    end_time = datetime.datetime.now()
    time_f.write(str(end_time) + " - кінець роботи з файлом\n")
    time_f.write('Витрачено часу на даний файл - ' + str(end_time - start_time) + '\n\n')

    return conn, cursor


time_file = open('time.txt', 'w')
conn, cursor = insert_data(2019, "Odata2019File.csv", conn, cursor, time_file)
conn, cursor = insert_data(2020, "Odata2020File.csv", conn, cursor, time_file)
time_file.close()


cursor.close()
conn.close()
