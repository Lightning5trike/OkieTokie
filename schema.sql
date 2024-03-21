DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL,
  customer_password TEXT NOT NULL
);

DROP TABLE IF EXISTS products;
CREATE TABLE products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  productName TEXT NOT NULL,
  product_section TEXT NOT NULL,
  product_image TEXT NOT NULL
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  collection_date TIMESTAMP NOT NULL,
  quantity TEXT,
  users_email TEXT,
  cake_size TEXT,
  extras TEXT,
  extra_info TEXT,
  layers TEXT,
  products_productName TEXT,
  FOREIGN KEY (users_email) REFERENCES users(email)
);
