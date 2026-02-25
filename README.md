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

cur.execute("SELECT \* FROM products;")
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
==> what happens when a file name will pip still works.
==> on closing cur.close() and conn.close() use to disconnect a connection.

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

sales per product sales = money made = sprice \* quantity join - pk = fk

select products.name as p_name , sum(products.selling_price \* sales.quantity) as total_sales from products join sales on sales.pid = products.id group by(p_name);

aggregate functions in sql sum() max() min() avg() count()

p_name | total_sales --------+------------- milk | 6380.00 bread | 1200.00 (2 rows)

n/b : when using aggregate functions in sql, you have to group by

select date(sales.created_at) as date , sum((products.selling_price - products.buying_price) as profit \* sales.quantity) from sales join products on products.id = sales.pid group by(date);

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

recap
CREATE A NEW PROJECT CALLED MYDUKA AND IN IT HAVE THE FOLLOWING FILES:
1.main.py
2.database.py

Open up a new terminal in VS Code and run the following:

- pip install flask
- pip install psycopg2-binary

Create a new database in sql shell called myduka_db

1.create database myduka_db;
2.connect to myduka_db database
\c myduka_db
3.Run the following commands to create tables

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
    );

//users table
CREATE TABLE users (
id SERIAL PRIMARY KEY,
full_name VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL UNIQUE,
phone_number VARCHAR(100) NOT NULL,
password VARCHAR(255) NOT NULL
);

WEB
server - a computer that provides data to other computers
hosting - renting a server to deploy resources and make them available to the internet
ip address - a unique number that identifies a device on a network
192.168.1.1 -ipv4
127.0.0.1
domain name - human friendly name for us to access an IP address
url -> full address of a resource on the internet
e.g. https://meet.google.com/dsh-idtb-oqb
protocol
domain
path - specific resource you want to access
port - where a service is running
http - not secure - sends data as plain text
https - secure - data is encrypted

192.168.1.1 -> www.google.com

**PSYCOPG2**
A PostgreSQL adapter / driver used to connect Python to a Postgres database
server, database, port ,username ,password

Python is connected to a Postgres db by psycopg2 using the function: psycopg2.connect()
psycopg2.connect() arguments
1.host - on what server is the database hosted /located
localhost - my local device
127.0.0.1
2.port - exactly where the Postgres service is running on my server
5432 - default port for Postgres service
3.user - username used to identify who is accessing the db(postgres)
4.password - password attached to the username to authenticate oneself before using Postgres services
5.dbname - what database are you connecting to

**cur** - an object used to perform database operations
DB OPERATIONS

1.

Next: - insert 2 products in sql shell
insert into products(name,buying_price,selling_price) values('milk',60,70);

cur.execute() - a cursor function to exectute sql queries
cur.fetchall() - a function that retrives data from the query and gives it to Python

Data from our db comes in the form of a **list of tuples**
Task:
1.Brush up on the following: sql queries , Python concepts(if ,for, lists, tuples,data types, type conversion, functions)

FUNCTIONS

- block of code used to perform a specific tasks
  Why use Functions?
  1.Modularity - breaking a large codebase into smaller programs
  2.Code organization
  3.Reusability of code
  4.Better debugging
  5.Scales well
  6.Readability

Global vs Local Space

Insert Syntax
insert into table_name(column1,column2,column3,...)values(value1,value2,value3,...)

Fetching vs Inserting Data
Fetching:
cur.execute(...your select query goes here)
cur.fetchall() - retrieves data from the db to Python

Inserting:
cur.execute(...your insert query goes here)
conn.commit() - commit / save data to the database permanently

TASK
Write a function that:
1.fetches data from your sales table - get_sales()
2.inserts sales into your sales table - insert_sale()

sales per day
sales per product
profit per product
profit per day

products table - id, product name , bprice ,sprice
sales - id, pid, quantity , created_at

sales per product
sales = money made = sprice \* quantity
join - pk = fk

select products.name as p_name , sum(products.selling_price \* sales.quantity) as total_sales from products join sales on sales.pid = products.id group by(p_name);

aggregate functions in sql
sum()
max()
min()
avg()
count()

p_name | total_sales
--------+-------------
milk | 6380.00
bread | 1200.00
(2 rows)

n/b : when using aggregate functions in sql, you have to group by

select date(sales.created_at) as date , sum((products.selling_price - products.buying_price) as profit \* sales.quantity) from sales join products on products.id = sales.pid group by(date);

TASK
1.Using functions:

- insert stock data using placeholders --- %s instead of using f-string (research)
- fetch stock data

  2.Using functions fetch the following data

- sales per day
  -profit per product

  **OBJECT ORIENTED PROGRAMMING**

We have the follwing broad categories of data types in Python:

1.Inbuilt data types - data types that come with the programming language

- int, float, str , lists, bool
  2.User defined data types - created by the programmer
- enabled by the use of classes and objects

_OOP_ - a paradigm that builds programs around classes and objects
_Class_ - a blueprint for creating objects
_Objects_ - an instance of a class

Any class has 2 things:
1.Data - attributes - variables holding data in a class - answers the question , what does a class have? - e.g. class Person -> name, age, email, dob, address
class car - make , yom , model

2.Behaviour - defined by _methods_ - _Method_ - a function inside a class - Behaviour answers the question, what can a class do? - e.g class Person - walk , talk, eat ,sleep , code
class Car - start , move ,stop

_Constructor_ - a special method used to initialize objects - it is automatically called when
an object is created - init()

dunder methods - double underscore methods

TASK
1.Create a class called BankAccount with the attributes: - account number , balance , owner name , date opened
2.Add some behaviour to the above class using the methods: - deposit() - withdraw() -display_info()
3.Create 2 BankAccount objects that can deposit , withdraw and display info

    *INHERITANCE*

-> This is the concept where one class inherits / acquires properties from another class
_Parent class_  
 -The class from which properties are inherited
-Also called Base class / Super class
_Child class_
-The class inheriting properties from a parent class
-Also called Derived class / Sub class

_Why Inheritance is Important?_
1.Code Reusability
2.Adds new features to an existing class
3.Allows behaviour modification - method overriding

_Types of Inheritance_
1.Single-level - a child inherits from a single parent class
2.Multiple inheritance - a child inheriting from more than one parent class
2.Multilevel inheritance - a child inherits from a parent class while also this parent class inherits from another parent
4.Hierrachial inheritance
-multiple child classes from a single parent class

_super_ -> a keyword that allows a child class to access parent methods and attributes

_Method Overriding_
This is where a child class provides its own implementation of a method that already exists in the
parent class - The child's method replaces the parent method when called by a child object
-> This is a form of POLYMORPHISM

Task
1.Create a Car Class Have the following attributes
brand - model - year -fuel_capcity - fuel_level -is_running(boolen value)
Have the following methods as behaviour for your class:
start()
stop()
refuel()
drive()
display_car_info()

2.Create child classes from parent class Car namely: Toyota & Audi and have them override the methods above

Pillars of OOP
1.Inheritance
2.Polymorphism
3.Abstraction
4.Encapsulation

_Introduction to Flask_
Framework vs Library

Framework - prebuilt code and tools used by developers to build applications without building from scratch
-> They easen development but require you to follow strict framework guidelines

Examples of Frameworks
1.Python - Flask, Django,FastAPI
2.C# - .NET
3.Java - Spring
4.JavaScript - React, Vue, Angular
5.Ruby - Ruby on Rails
6.Golang - Chi, Gin
7.NodeJS - Express
8.PHP - Laravel

1.Routing in Flask
-> This is a mechanism to map / connect URLs to Python functions. This is a system for resource navigation
-> To achieve routing in Flask we use decorator functions
-> Decorator : @app.route()

URLs
The full address used to access an aplication through the web

Parts of URL
1.Protocol - http / https
2.Domain - name of the application
3.Path - resource to be accessed
4.Port - specific location where an app is running\

https://meet.google.com/dsh-idtb-oqb

_Decorator functions_
-> A decorator function is function that modifies /determines the behaviour of another function
-> They are usually preceded by the'@' character
-> This decorator function can take some parameters :
1.Path - specific resource to be accessed
2.Method

_view function_ - a function responsible for retturnng resources to the client

@app.route('/products') -> decorator function
def products(): -> view function
return "Login Page" -> resource to be returned

N/B : -> We cant have two routes having the same view function name

_RENDERING HTML PAGES IN FLASK_
-> Instead of returning single data items , we'd rather return full html pages to the client
-> To render html pages using flask , we use a function called render*template()
-> \_Template* - a single html page
-> render_template() -> takes as am argument , the name of a html file you wish to return

Project Structure
static - contains all css files
templates -> contains all html files
-index.html
-products.html
..
database.py
main.py

static and templates folders have to be named exactly like that and all css / html files
must be contained in them ---> this is due to strict framework rules

_JINJA_
-> A templating engine integrated with Flask to render dynamic html pages
-> A syntax used to render Pthon data in html

_How to use Jinja_
Has 2 cases

1.When displaying variables - use two curly braces

- {{}}
  name = "Jake"
  {{name}}
  2.When using Control Structures
  -> use the following syntax: {% %}
  -> For Jinja in control structures, you need to have a starting point and an ending point

         {% for i in products%} - initialization
              .....
          {% endfor %} - termination

          {% if... %}
             ...
          {% else %}
             ...
          {% endif %}

_Control Structures_
-> Building blocks that determine the flow and execution of a program
1.Sequence
-> A program executes top to bottom , left to right
2.Repitition
-> Iteration - loops
3.Selection
-> Conditional statements - if -else

TASK
1.Render sales data in a sales table inside the sales page

_Template Inheritance_
-This is the concept of reducingg redundancy in creating html pages with flask by having one template called base
which contains all common features of every page
->Template inheritance is largely supported by Jinja

_Why use Template Inheritance_
1.Simplifies development
2.Reduces redundancy
3.Uniformity

_How to apply template inheritance_
1.Create a parent template e.g base.html, layout.html
2.Create blocks to allow for each page's unique content
3.In the children templates, inherit features from the base using the keyword extends
3.Use blocks to render content

    {% block title %} -> TITLE OF EACH PAGE GOES HERE <- {% endblock %}


      {% block content %}

        -> each page's unique content goes here

      {% endblock %}

TASK
1.Apply template inheritance across every other page

_RENDERING DATA IN DATA TABLES_

INSERTING DATA FROM A CLIENT
1.User form in html -contains inputs of data to be inserted e.g.
inserting products
-form => inputs => product name, buying price , selling_price, button of type submit

2.Route in main.py to process data insertion e.g @app.route('/add_products) def add_products(): ......

3.An insert function defined in database.py - contains insert query def insert_products(values): ......

Form Checklist in data insertion

1.method attribute Method - determines what a server does to a resource / data
-> GET - retrieving data from a server
-> POST - send data to a server
-> PUT - update an existing resource
-> DELETE - get rid of a resource

2.action attribute action - determines the route in which form data is submitted - in what route is my form data submitted and processed 

3.name attribute N/B -> Data sent from the form is sent in key-value pairs -> The server needs to know from what input each value came from -> The server uses the key to extract form data filled by the user --> This key is defined by the value of the name attribute 4.input type - determines what data type is filled in an input 5.button -of type submit

"p_name":eggs "b_price":15 "s_price":20

Workflow to insert data 1.User is provided with a form 2.User fills and submits the form 3.Form is submitted to the route specified in action -> the route needs to have methods = ['GET','POST'] - defines what a server can do in this route 4.Form data is extracted by a request object -> request object has access to some methods: => request.method : determines what method is used in the form => request.form : extracts form data from the form using its key(from name attribute)
5.Data is processed and inserted into your db 6.User is redirected redirect - take a user to another resource redirect() - takes as a parameter another function called url_for => redirect(url_for('name of view function ')) redirect(url_for('products')) 7.Server gives a feedback on the process. status code - special numbers that communicate server actions Categories of status codes 100 - 199 => general informational responses 200 - 299 => successful responses 300 - 399 => redirection messages 400 - 499 => client error 500 - 599 = server error

TASK -> Post sales using a sales form, confirm sales data reflects in sales table
