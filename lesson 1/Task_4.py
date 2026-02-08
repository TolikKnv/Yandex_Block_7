import sqlite3

con = sqlite3.connect("db.sqlite")
cur = con.cursor()

# Напишите SQL запрос в строке.
results_1 = cur.execute(
    """
SELECT MIN(price)
FROM ice_cream;
"""
)


results_2 = cur.execute(
    """
SELECT AVG(price)
FROM ice_cream
WHERE category = 'Экзотическое';
"""
)

results_3 = cur.execute(
    """
SELECT SUM(price)
FROM ice_cream
WHERE is_published = 1 AND is_on_main = 1;
"""
)


# for result in results:
#     print(result)

con.close()
