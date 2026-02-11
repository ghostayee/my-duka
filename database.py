import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="Ford6000$$$...",
    dbname="myduka_db",
)


cur = conn.cursor()

cur.execute("select * from products")
products = cur.fetchall()
print(products)