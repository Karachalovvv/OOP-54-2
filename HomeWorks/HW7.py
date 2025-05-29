import sqlite3

# Альбом из А4 листов
connect = sqlite3.connect("users.db")


# Рука у которой есть карандаш
cursor = connect.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
""")

connect.commit()


# CRUD - Create - Read - Update - Delete

def add_user(name: str, age: int, hobby = "None"):

    cursor.execute(
        f"INSERT INTO users(name, age, hobby) VALUES (?,?,?)",
        (name, age, hobby)
    )
    connect.commit()
    print(f"{name} - добавили")


# add_user("Chyngyz", 26, "Спать")
# add_user("User1", 26, "Спать")
# add_user("User2", 26, "Спать")
# add_user("User3", 26, "Спать")
# add_user("User4", 26, "Спать")


def get_all_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print(users)

    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")

get_all_users()

def update_user(name, rowid):
    cursor.execute("UPDATE users SET name = ? WHERE rowid = ?",
                   (name, rowid)
    )
    connect.commit()
    print("Обновлен пользователь!!")

# update_user("Arzybek", 6)

def delete_user(rowid):
    cursor.execute(
        "DELETE FROM users WHERE rowid = ?",
        (rowid,)
    )
    connect.commit()
    print("Пользователь удален!!")

# delete_user(2)

def get_user_by_id(user_id):

    cursor.execute("SELECT * FROM users WHERE rowid = ?", (user_id,))
    user = cursor.fetchone()

    if user:
        print(f"ID: {user[0]}, NAME: {user[1]}, AGE: {user[2]}, HOBBY: {user[3]}")

    else:
        print(None)

get_user_by_id(10)

