CREATE A NEW PROJECT CALLED MYDUKA AND IN IT HAVE THE FOLLOWING FILES: 1.main.py 2.database.py

Open up a new terminal in VS Code and run the following:

pip install flask
pip install psycopg2-binary
Create a new database in sql shell called myduka_db

1.create database myduka_db; 2.connect to myduka_db database \c myduka_db 3.Run the following commands to create tables

 //products table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    buying_price NUMERIC(20, 2) NOT NULL CHECK (buying_price >= 0),
    selling_price NUMERIC(20, 2) NOT NULL CHECK (selling_price >= 0)
);

//stock table
CREATE TABLE stock (
    id SERIAL PRIMARY KEY,
    pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    stock_quantity INTEGER NOT NULL CHECK (stock_quantity >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

//sales table
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

own shit on mysql shell master the basic of it.


on the task to brush on NB
==>basic commands in sql
  SELECT ==> retrieve data
  INSERT INTO ==> add new record
  UPDATE ==> modify existing record
  DELETE ==> remove records.

WHERE ==> filters rows
ORDER BY ==> sort results
GROUP BY ==> aggregate rows
JOIN ==> combine data g=from multiple tables

import psycopg2
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="mypassword",
    dbname="mydb"
)
cur = conn.cursor()

on execution of queries
cur.execute("SELECT * FROM products;")
rows = cur.fetchall()
for row in rows:
    print(row)
