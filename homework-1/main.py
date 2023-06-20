"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

with psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="goldbaby1987@") as conn:
    with conn.cursor() as cur:
        with open('./north_data/customers_data.csv') as file:
            reader = csv.DictReader(file, delimiter=",").reader
            next(reader)
            for x in reader:
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", x)
            conn.commit()
        with open('./north_data/employees_data.csv') as file:
            reader = csv.DictReader(file, delimiter=",").reader
            next(reader)
            for x in reader:
                print(x)
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", x)
            conn.commit()

        with open('./north_data/orders_data.csv') as file:
            reader = csv.DictReader(file, delimiter=",").reader
            next(reader)
            for x in reader:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", x)
            conn.commit()
