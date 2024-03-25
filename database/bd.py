import sqlite3
import aiosqlite

db = sqlite3.connect('tg.db')
cur = db.cursor()

#Создание базы данных
async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "user_id INTEGER, "
                "brawl_id_1 TEXT, "
                "brawl_name_1 TEXT,"
                "brawl_id_2 TEXT,"
                "brawl_name_2 TEXT,"
                "brawl_id_3 TEXT,"
                "brawl_name_3 TEXT)")
    db.commit()

    
#Функция для добавления user id
async def save_user_id(user_id):
    user = cur.execute("SELECT * FROM accounts WHERE user_id == {key}".format(key = user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (user_id) VALUES ({key})".format(key = user_id))
        db.commit()


#Проверка есть лы такой user id в базе данных и если да то возвращает brawl id
async def get_brawl_id_1(user_id):
    user = cur.execute("SELECT * FROM accounts WHERE user_id == ?", (user_id,)).fetchone()
    if user is not None:
        return user[1]
    else:
        return "False"

async def get_brawl_id_2(user_id):
    user = cur.execute("SELECT * FROM accounts WHERE user_id == ?", (user_id,)).fetchone()
    if user is not None:
        return user[3]
    else:
        return "False"

async def get_brawl_id_3(user_id):
    user = cur.execute("SELECT * FROM accounts WHERE user_id == ?", (user_id,)).fetchone()
    if user is not None:
        return user[5]
    else:
        return "False"


#Проверка есть лы такой user id в базе данных и если да то возвращает brawl name
async def get_brawl_name_1(user_id):
    user = cur.execute("SELECT * FROM accounts WHERE user_id == ?", (user_id,)).fetchone()
    if user is not None:
        return user[2]
    else:
        return "False"

async def get_brawl_name_2(user_id):
    user = cur.execute("SELECT * FROM accounts WHERE user_id == ?", (user_id,)).fetchone()
    if user is not None:
        return user[4]
    else:
        return "False"

async def get_brawl_name_3(user_id):
    user = cur.execute("SELECT * FROM accounts WHERE user_id == ?", (user_id,)).fetchone()
    if user is not None:
        return user[6]
    else:
        return "False"
    

#Добавление brawl_id_1 по user id
async def save_brawl_stars_id_1(user_id, brawl_id):
    cur.execute("UPDATE accounts SET brawl_id_1 = ? WHERE user_id = ?", (brawl_id, user_id))
    db.commit()
async def save_brawl_stars_id_2(user_id, brawl_id):
    cur.execute("UPDATE accounts SET brawl_id_2 = ? WHERE user_id = ?", (brawl_id, user_id))
    db.commit()
async def save_brawl_stars_id_3(user_id, brawl_id):
    cur.execute("UPDATE accounts SET brawl_id_3 = ? WHERE user_id = ?", (brawl_id, user_id))
    db.commit()

#Добавление brawl_name_1
async def save_brawl_stars_name_1(brawl_name, user_id):
    cur.execute("UPDATE accounts SET brawl_name_1 = ? WHERE user_id = ?", (brawl_name, user_id))
    db.commit()
async def save_brawl_stars_name_2(brawl_name, user_id):
    cur.execute("UPDATE accounts SET brawl_name_2 = ? WHERE user_id = ?", (brawl_name, user_id))
    db.commit()
async def save_brawl_stars_name_3(brawl_name, user_id):
    cur.execute("UPDATE accounts SET brawl_name_3 = ? WHERE user_id = ?", (brawl_name, user_id))
    db.commit()

async def clear_all_cells():
    async with aiosqlite.connect('tg.db') as db:
        async with db.cursor() as cur:
            # Получаем все имена таблиц
            await cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = await cur.fetchall()

            for table in tables:
                # Удаляем все строки из каждой таблицы
                await cur.execute(f"DELETE FROM {table[0]};")
            
            await db.commit()




