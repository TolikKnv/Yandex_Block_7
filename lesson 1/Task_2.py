# 1
# import sqlite3

# con = sqlite3.connect("db.sqlite")
# cur = con.cursor()

# # Напишите SQL запрос в строке.
# cur.execute(
#     """
#     SELECT tbl_name FROM sqlite_master WHERE type = 'table';
# """
# )

# table = cur.fetchall()[0][0]  # Получите имя таблицы через атрибут курсора.

# # Напишите SQL запрос в строке.
# results = cur.execute(
#     f"""
# SELECT full_name
# FROM {table};
# """
# )


# for result in results:
#     print(result)

# con.close()


# 2
import sqlite3

con = sqlite3.connect("db.sqlite")
cur = con.cursor()

# Напишите SQL запрос в строке.
results = cur.execute(
    """
SELECT title FROM ice_cream WHERE is_published = 1 AND is_on_main = 1
"""
)


for result in results:
    print(result)


con.close()
