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
conn.commit()


def my_query():
    select_query = '''
        SELECT student.regname as Region, 
		year, 
		AVG(physBall100) as Avg_phys_ball
        FROM test_info
        
		INNER JOIN student on test_info.outid = student.outid
		WHERE physTestStatus = 'Зараховано'
        GROUP BY REGNAME, year;
        '''
    cursor.execute(select_query)

    with open('result.csv', 'w', encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Область', 'Рік', 'Середній бал з фізики'])
        for row in cursor:
            csv_writer.writerow(row)


my_query()
