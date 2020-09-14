#import psycopg2  # !pip install psycopg2
import mysql.connector as mysql  # pip install mysql-connector-python

SQL_DETECT_IDIOM = "SELECT DISTINCT(dc_language) FROM repositorio.tme WHERE dispquery = 'True';"


class Tme:
    def __init__(self, db):
        self.__db = db

    def idiom():
        conn = mysql.connect(host='127.0.0.1', port='3306', database='repositorio', user='root', password='203501')
        cursor = conn.cursor()
        cursor.execute(SQL_DETECT_IDIOM)
        idioms = [item[0] for item in cursor.fetchall()]
        cursor.close()  # Close communication with the database
        conn.close()
        return idioms





