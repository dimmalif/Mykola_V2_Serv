import sqlite3 as sq


def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


async def db_start():

    db = sq.connect('user.db')
    curs = db.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, audio_command BLOB)")
    db.commit()


async def create_profile(user_id):
    db = sq.connect('user.db')
    curs = db.cursor()
    user = curs.execute('SELECT 1 FROM profile WHERE user_id == "{key}"'.format(key=user_id)).fetchall()
    if not user:
        curs.execute('INSERT INTO profile VALUES(?, ?)', (user_id, ''))
        db.commit()
    db.close()


async def edit_profile(user_id, audio):
    db = sq.connect('user.db')
    curs = db.cursor()
    audio_file = convert_to_binary_data(audio)
    data = (user_id, audio_file)
    query = 'INSERT INTO profile VALUES (? ?)'
    curs.execute('INSERT INTO profile VALUES (? ?)'.format(user_id, audio_file))
    # curs.execute("UPDATE profile WHERE user_id == '{}' SET audio_command = '{}' ".format(user_id, audio_file))
    db.commit()
    db.close()

