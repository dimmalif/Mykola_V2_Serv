# import sqlite3, os
#
# resume = 'derix035.wav'
#
# db = sqlite3.connect('sqlite_python.db')
# curs = db.cursor()
# curs.execute("CREATE TABLE IF NOT EXISTS profile (name TEXT PRIMARY KEY, resume BLOB NOT NULL)")
# db.commit()
# db.close()
#
#
# def convert_to_binary_data(filename):
#     # Преобразование данных в двоичный формат
#     with open(filename, 'rb') as file:
#         blob_data = file.read()
#     return blob_data
#
#
# def insert_blob(full_name, name, resume_file):
#     sqlite_connection = sqlite3.connect('sqlite_python.db')
#     cursor = sqlite_connection.cursor()
#     print("Подключен к SQLite")
#
#     sqlite_insert_blob_query = """INSERT INTO new_employee
#                               (id, name, resume) VALUES (?, ?, ?)"""
#
#     resume = convert_to_binary_data(resume_file)
#     # Преобразование данных в формат кортежа
#     data_tuple = (full_name, name, resume)
#     cursor.execute(sqlite_insert_blob_query, data_tuple)
#     sqlite_connection.commit()
#     print("Изображение и файл успешно вставлены как BLOB в таблиу")
#     cursor.close()
#
#     if sqlite_connection:
#         sqlite_connection.close()
#         print("Соединение с SQLite закрыто")
#
#




# Конвертація валют
import requests


to = 'UAH'
fromm = 'EUR'

url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={fromm}&amount={150}"

payload = {}
headers= {
  "apikey": "YmONMZ6RphSU1LaXeQ9rwvgLBg83jakw"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)
