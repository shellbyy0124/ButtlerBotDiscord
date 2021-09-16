import sqlite3

def create_db():
    conn = sqlite3.connect('main.db')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS guild_info(
            guild_id INT,
            member_count INT
        )''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS profiles(
            guild_id INT,
            member_id INT,
            member_name TEXT,
            member_nick TEXT,
            fav_color TEXT,
            langs TEXT
        )''')

    conn.commit()
    conn.close()