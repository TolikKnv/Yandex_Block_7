import sqlite3

con = sqlite3.connect("db_ice_cream.sqlite")

cur = con.cursor()

cur.executescript(
    """
CREATE TABLE IF NOT EXISTS ice_cream(
id INTEGER PRIMARY KEY,
title TEXT,
description TEXT,
wrapper_id INTEGER NOT NULL UNIQUE,
FOREIGN KEY (wrapper_id) REFERENCES wrapper(id)
);

CREATE TABLE IF NOT EXISTS wrapper(
id INTEGER PRIMARY KEY,
title TEXT
);
"""
)
con.close()


con = sqlite3.connect("db.sqlite")

cur = con.cursor()

results = cur.execute(
    """
SELECT ice_cream.title, wrappers.title
FROM ice_cream, wrappers
WHERE ice_cream.wrapper_id = wrappers.id
AND wrappers.title LIKE 'Б%';
"""
)

for result in results:
    print(result)

con.close()
