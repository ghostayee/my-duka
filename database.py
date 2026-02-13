import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="Ford6000$$$...",
    dbname="myduka_db",
)


cur = conn.cursor()

def get_data(table):
    cur.execute(f"select * from {table}")
    data = cur.fetchall()
    return data

data = get_data("sales")
print(data)


def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

products = get_products()
print(products)

def insert_products(values):
    cur.execute("insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()



product1 = ('butter',90,95)
product2 = ('iphone',455,470)

insert_products(product1)
