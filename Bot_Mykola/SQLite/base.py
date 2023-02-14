import sqlite3 as sq


async def db_start():

    db = sq.connect('user.db')
    curs = db.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS profile(user_id PRIMARY KEY, full_name NOT NULL, username TEXT, city TEXT,"
                 "last_date TEXT, report )")
    db.commit()
    db.close()


async def create_profile(user_id: str, full_name: str, username: str) -> None:
    db = sq.connect('user.db')
    curs = db.cursor()
    user = curs.execute('SELECT 1 FROM profile WHERE username == "{key}"'.format(key=username)).fetchall()
    if not user:
        curs.execute('INSERT INTO profile VALUES(?, ?, ?, ?, ?)', (user_id, full_name, username, '', ''))
        db.commit()
    db.close()


def lust_time(user_id, time: str) -> None:
    db = sq.connect('user.db')
    curs = db.cursor()

    sqlite_insert_time = """INSERT OR REPLACE INTO profile
                              (user_id, time) VALUES (?, ?)"""
    data_tuple = (user_id, time)

    curs.execute(sqlite_insert_time, data_tuple)
    db.commit()
    db.close()


def add_city(user_id, position: str) -> None:
    db = sq.connect('user.db')
    curs = db.cursor()
    curs.execute(f"UPDATE profile SET city = '{position}' WHERE user_id LIKE {user_id}")
    db.commit()
    db.close()


def get_city(user_id) -> list: # need rename
    db = sq.connect('user.db')
    curs = db.cursor()
    curs.execute('SELECT city FROM profile WHERE user_id = ?', [int(user_id)])
    city = curs.fetchall()
    # city = curs.execute('SELECT 1 FROM profile WHERE username == "{key}"'.format(key=user_id)).fetchall()
    db.commit()
    print(city)
    return city
    # db.close()


def get_report(user_id, rep: str) -> None:
    db = sq.connect('user.db')
    curs = db.cursor()
    curs.execute(f"UPDATE profile SET report = '{rep}' WHERE user_id LIKE {user_id}")
    db.commit()
    db.close()
