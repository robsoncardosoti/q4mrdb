import psycopg2  # !pip install psycopg2

SQL_DETECT_IDIOM = "SELECT DISTINCT(dc_language) FROM public.tme WHERE dispquery = 'True';"
SQL_METADADOS = 'SELECT id, nome, categoria, console from jogo' #'select dc_title from tme'


class Tme:
    def __init__(self, db):
        self.__db = db

    def idiom():
        conn = psycopg2.connect(host='127.0.0.1', port='5432', database='tme', user='tme', password='q4dbrm')
        cursor = conn.cursor()
        cursor.execute(SQL_DETECT_IDIOM)
        idioms = [item[0] for item in cursor.fetchall()]
        cursor.close()  # Close communication with the database
        conn.close()
        return idioms





