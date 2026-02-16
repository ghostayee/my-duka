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
print(rows)


what are the time when NOT NULL cannot apply.
like email not everybody has email

date when inserting teh year comes first thn month then day
year, month, day with DATE as reserved word.

selling_price NUMERIC(20, 2) NOT NULL CHECK (selling_price >= 0)
==> the 20 means max length digits including the decimals.
==> 2 decimal places
==> numeric specifies the data type.
==> checks ensures that no negative price.
==> serial automatically generates id.
==> primary key

NB\ REFERENCES products(id) creates a foreign key linking this table to the id column in the products table. This enforces relational integrity: the pid must exist in products.

ON DELETE CASCADE means if a product is deleted from products, all rows in this table with that pid will also be automatically deleted. This prevents orphan records
date '1990-12-31'

delete from deletes the data but keeps the structure
where clause. its a condition.





insert syntax

insert into table_name(column1, .........)values(value1.....)


the sql \d looks out at the table.
==>  what happens when a file name will pip still works.
==> on closing cur.close() and conn.close()  use to disconnect a connection.

the task on extraction of data and profit.
sales per product group by product sum units x selling price
sales per day group by date

==> profit per product
==> profit per day