from aiogram import types, Dispatcher
from aiogram.types import message
import sqlite3 as sq

db = sq.connect('user.db')
curs = db.cursor()
# curs.execute('ALTER TABLE profile DROP COLUM ')
user_id = 469156495

curs.execute('SELECT * FROM profile WHERE user_id = ?', [user_id])
city = curs.fetchall()
print(city)
db.commit()
db.close()
