import sqlite3


conn = sqlite3.connect('database.db')
cur = conn.cursor()

#opens connection to schema file and puts data into database
with open('schema.sql') as f:
    conn.executescript(f.read())

#inserts these bits of data into the different databases
cur.execute("INSERT INTO users (email, customer_password) VALUES ('Oyinda.Kuti@learnatwren.org', 'crochet123')")
cur.execute("INSERT INTO users (email, customer_password) VALUES ('Tomisin.sadiq-ajala@learnatwren.org', 'Sasuke456')")

cur.execute("INSERT INTO products (productName, product_section, product_image) VALUES ('regular fudgy brownie', 'brownies', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPHVecB40QqZwDafdqkjJrOZMb2wyQuqmgUw&usqp=CAU')")
cur.execute("INSERT INTO products (productName, product_section, product_image) VALUES ('oreo brownie', 'brownies', 'https://www.shugarysweets.com/wp-content/uploads/2021/04/oreo-brownies-recipe-735x735.jpg')")
cur.execute("INSERT INTO products (productName, product_section, product_image) VALUES ('brownie cookie combo', 'brownies', 'https://www.justataste.com/wp-content/uploads/2020/07/the-best-chocolate-chip-cookie-brownies.jpg')")

cur.execute("INSERT INTO products (productName, product_section, product_image) VALUES ('plain sugar cookies', 'cookie', '')")
cur.execute("INSERT INTO products (productName, product_section, product_image) VALUES ('triple chocolate cookie', 'cookie', '')")
cur.execute("INSERT INTO products (productName, product_section, product_image) VALUES ('chocolate chip cookie', 'cookie', '')")

cur.execute("INSERT INTO products (productName, product_section, product_image) VALUES ('vanilla cupcakes with vanilla frosting', 'cupcakes', '')")
cur.execute("INSERT INTO products (productName, product_section, product_image) VALUES ('vanilla cupcakes with chocolate frosting', 'cupcakes', '')")
cur.execute("INSERT INTO products (productName, product_section, product_image) VALUES ('vanilla cupcakes with rainbow frosting', 'cupcakes', '')")
cur.execute("INSERT INTO products (productName, product_section, product_image) VALUES ('chocolate cupcakes with vanilla frosting', 'cupcakes', '')")
cur.execute("INSERT INTO products (productName, product_section, product_image) VALUES ('chocolate cupcakes with chocolate frosting', 'cupcakes', '')")
cur.execute("INSERT INTO products (productName, product_section, product_image) VALUES ('chocolate cupcakes with rainbow frosting', 'cupcakes', '')")



#commiting to the table and then closing the connection
conn.commit()
conn.close()
