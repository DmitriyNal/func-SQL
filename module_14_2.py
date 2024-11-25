import sqlite3

connection = sqlite3.connect('not_telegram.db')

''' Создание объекта курсора'''
cursor = connection.cursor()

"""Создание таблицы"""
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# cursor.execute('''CREATE INDEX IF NOT EXISTS ind_email on Users(email)''')
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?,?,?,?)",
#                    (f'User{i}', f'example{i}@gmail.com', i * 10, 1000))
# cursor.execute(''' UPDATE Users SET balance =500 WHERE id%2=1''')
#
# cursor.execute('''DELETE FROM Users WHERE id%3=1''')
#
# """ Выполнение SQL запроса"""
# cursor.execute('''SELECT username,email, age, balance FROM Users WHERE age !=60''')
#
# '''Получение всех записей'''
# records = cursor.fetchall()

cursor.execute('''DELETE FROM Users WHERE id=6''')
cursor.execute('''SELECT COUNT(*) FROM Users''')
total = cursor.fetchone()[0]
print(total)
cursor.execute('''SELECT SUM(balance) FROM Users''')
sum_balance = cursor.fetchone()[0]
print(sum_balance)
cursor.execute('''SELECT AVG(balance) FROM Users''')
avg_balance = cursor.fetchone()[0]
print(avg_balance)
connection.commit()
'''Закрытие соединения с базой данных'''
connection.close()