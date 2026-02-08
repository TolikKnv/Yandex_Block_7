import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Напишите SQL запрос в строке.
results = cur.execute('''
SELECT category, AVG(price)
FROM ice_cream
GROUP BY category;
''')


for result in results:
    print(result)

con.close()