import sqlite3 as sq


async def db_start():
    global db, curs

    db = sq.connect('user.db')
    curs = db.cursor()

    curs.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, username TEXT)")

    db.commit()


async def create_profile(user_id):
    user = curs.execute('SELECT 1 FROM profile WHERE user_id == "{key}"'.format(key=user_id)).fetchall()
    if not user:
        curs.execute('INSERT INTO profile VALUES(?, ?)', (user_id, ''))
        db.commit()


async def edit_profile(state, user_id):
    async with state.proxy() as data:
        curs.execute("UPDATE profile WHERE user_id == '{}' SET username = '{}, ' ".format(user_id, data['username']))
        db.commit()
