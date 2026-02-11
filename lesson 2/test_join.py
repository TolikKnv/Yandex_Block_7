import sqlite3

con = sqlite3.connect("db_video_type_slogan.sqlite")
cur = con.cursor()


result = cur.execute(
    """
-- Верни все поля
SELECT *
-- из таблицы video_products
FROM video_products
-- ...но перед этим присоедини записи из таблицы slogans так, чтобы
-- в записях значения полей video_products.slogan_id и slogans.id были равны.
JOIN slogans ON video_products.slogan_id = slogans.id;
"""
)

for item in result:
    print(item)

print()

result_2 = cur.execute(
    """
SELECT video_products.title,
       slogans.slogan_text,
       product_types.title
FROM video_products
JOIN slogans ON video_products.slogan_id = slogans.id
JOIN product_types ON video_products.type_id = product_types.id;
    """
)

for item in result_2:
    print(item)

print()

result_3 = cur.execute(
    """
SELECT video_products.title,
       slogans.slogan_text
FROM video_products
LEFT JOIN slogans ON video_products.slogan_id = slogans.id;
"""
)

for item in result_3:
    print(item)

print()

result_4 = cur.execute(
    """
SELECT video_products.title,
       product_types.title
FROM video_products
RIGHT JOIN product_types ON video_products.type_id = product_types.id;
"""
)

for item in result_4:
    print(item)

print()

result_5 = cur.execute(
    """
SELECT video_products.title,
       slogans.slogan_text
FROM video_products
FULL JOIN slogans ON video_products.slogan_id = slogans.id;
"""
)

for item in result_5:
    print(item)

print()

result_6 = cur.execute(
    """
SELECT video_products.title,
       slogans.slogan_text
FROM video_products
CROSS JOIN slogans;
"""
)

for item in result_6:
    print(item)

print()

