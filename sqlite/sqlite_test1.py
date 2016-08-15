import sqlite3

connection = sqlite3.connect('temp.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE products (name text, price integer);''')

cursor.execute('''INSERT INTO products (name, price) VALUES ('apple', 198);''')

cursor.execute('''INSERT INTO products (name, price) VALUES ('orange', 100);''')

connection.commit()

cursor.execute('''SELECT * FROM products;''')
products = cursor.fetchall()

print(type(products))   # -> "<type 'list>"
print(products)         # -> "[{u'apple',198}, {u'orange', 100}]"

print(products)
print(type(products))
