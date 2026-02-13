import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="Ford6000$$$...",
    dbname="my_duka"
)

cur = conn.cursor()


def get_data():
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    return(data)

data = get_data()
print(data)


def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

products = get_products()
print(products)