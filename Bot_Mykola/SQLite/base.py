import sqlite3 as sq

audio_command = 'derix035.wav'

def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


async def db_start():

    db = sq.connect('user.db')
    curs = db.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS profile(full_name, user_id TEXT PRIMARY KEY, audio_command BLOB, comands TEXT)")
    db.commit()
    db.close()


async def create_profile(full_name, user_id):
    db = sq.connect('user.db')
    curs = db.cursor()
    user = curs.execute('SELECT 1 FROM profile WHERE user_id == "{key}"'.format(key=user_id)).fetchall()
    if not user:
        curs.execute('INSERT INTO profile VALUES(?, ?, ?)', (full_name, user_id, ''))
        db.commit()
    db.close()


def insert_blob(full_name, name, audio_command):
    sqlite_connection = sq.connect('user.db')
    cursor = sqlite_connection.cursor()

    sqlite_insert_blob_query = """INSERT OR REPLACE INTO profile
                              (full_name, user_id, audio_command) VALUES (?, ?, ?)"""

    audio = convert_to_binary_data(audio_command)

    data_tuple = (full_name, name, audio)
    cursor.execute(sqlite_insert_blob_query, data_tuple)
    sqlite_connection.commit()
    sqlite_connection.close()

