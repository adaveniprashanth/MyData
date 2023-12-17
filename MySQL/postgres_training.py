import psycopg2

connection = psycopg2.connect(database="postgres",user="postgres",password="admin",port=5432)
cursor = connection.cursor()
