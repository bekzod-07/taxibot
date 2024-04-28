import sqlite3 as sql

def create_tabletosh():
    conn = sql.connect("data.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS tosh(toshkent TEXT)""")
    conn.commit()
    conn.close()

def create_tablejizz():
    conn = sql.connect("data.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS jizz(Jizzax TEXT)""")
    conn.commit()
    conn.close()

# Ma'lumot qo'shish
def add_to_databasejizz(Jizzax):
    conn = sql.connect("data.db")
    c = conn.cursor()
    c.execute("""INSERT INTO jizz VALUES (?)""", (Jizzax,))
    conn.commit()
    conn.close()

def add_to_databasetosh(Toshkent):
    conn = sql.connect("data.db")
    c = conn.cursor()
    c.execute("""INSERT INTO tosh VALUES (?)""", (Toshkent,))
    conn.commit()
    conn.close()

# Ma'lumotlarni olish
def get_data_jizz():
    conn = sql.connect("data.db")
    c = conn.cursor()
    c.execute("""SELECT * FROM jizz""")
    data = c.fetchall()
    conn.close()
    return data if data else []

def get_data_tosh():
    conn = sql.connect("data.db")
    c = conn.cursor()
    c.execute("""SELECT * FROM tosh""")
    data = c.fetchall()
    conn.close()
    return data if data else []

add_to_databasetosh("Toshkent")
add_to_databasejizz("Jizzax")

create_tabletosh()
create_tablejizz()
