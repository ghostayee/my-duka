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
==>




Global vs Local Space

Insert Syntax insert into table_name(column1,column2,column3,...)values(value1,value2,value3,...)

Fetching vs Inserting Data Fetching: cur.execute(...your select query goes here) cur.fetchall() - retrieves data from the db to Python

Inserting: cur.execute(...your insert query goes here) conn.commit() - commit / save data to the database permanently

TASK Write a function that: 1.fetches data from your sales table - get_sales() 2.inserts sales into your sales table - insert_sale()

sales per day sales per product profit per product profit per day

products table - id, product name , bprice ,sprice sales - id, pid, quantity , created_at

sales per product sales = money made = sprice * quantity join - pk = fk

select products.name as p_name , sum(products.selling_price * sales.quantity) as total_sales from products join sales on sales.pid = products.id group by(p_name);

aggregate functions in sql sum() max() min() avg() count()

p_name | total_sales --------+------------- milk | 6380.00 bread | 1200.00 (2 rows)

n/b : when using aggregate functions in sql, you have to group by

select date(sales.created_at) as date , sum((products.selling_price - products.buying_price) as profit * sales.quantity) from sales join products on products.id = sales.pid group by(date);

TASK 1.Using functions:

insert stock data using placeholders --- %s instead of using f-string (research)
fetch stock data
2.Using functions fetch the following data

sales per day -profit per product

OBJECT ORIENTED PROGRAMMING

We have the follwing broad categories of data types in Python:

1.Inbuilt data types - data types that come with the programming language

int, float, str , lists, bool 2.User defined data types - created by the programmer
enabled by the use of classes and objects
OOP - a paradigm that builds programs around classes and objects Class - a blueprint for creating objects Objects - an instance of a class

Any class has 2 things: 1.Data - attributes - variables holding data in a class - answers the question , what does a class have? - e.g. class Person -> name, age, email, dob, address class car - make , yom , model

2.Behaviour - defined by methods - Method - a function inside a class - Behaviour answers the question, what can a class do? - e.g class Person - walk , talk, eat ,sleep , code class Car - start , move ,stop

Constructor - a special method used to initialize objects - it is automatically called when an object is created - init() self - refers to the object being created

dunder methods - double underscore methods

TASK 1.Create a class called BankAccount with the attributes: - account number , balance , owner name , date opened 2.Add some behaviour to the above class using the methods: - deposit() - withdraw() -display_info() 3.Create 2 BankAccount objects that can deposit , withdraw and display info



THE WEEKEND RECAP
python ======> postgres_db through psycopg2.connect()
the arguments.
=>host
=>