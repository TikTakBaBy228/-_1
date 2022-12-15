#Модуль SQLite. Часть 3

import sqlite3

def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d


db = sqlite3.connect('test_db.sqlite')
db.row_factory = dict_factory
cursor = db.cursor()

email = 'petrov@gmail.com'

# cursor.execute(f"SELECT * FROM users WHERE email = '{email}' ")
# cursor.execute("SELECT * FROM users WHERE email = ?", [email])
# cursor.execute("SELECT * FROM users WHERE email = ? OR name = ?", (email, 'John Doe'))
cursor.execute("SELECT * FROM users")
#
res = cursor.fetchall()
#
# for user in res:
#     print(user[1], user[2])

for user in res:
    print(user['name'], user['email'])

print(res)




db.close()