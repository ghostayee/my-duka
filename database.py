import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="Ford6000$$$...",
    dbname="myduka_db"
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
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()



product1 = ('butter',90,95)
product2 = ('iphone',455,470)
product3 = ('lite',400,450)

insert_products(product1)
insert_products(product2)

item = input("Item_name:")
buying = int(input("Buying_price:"))
selling = int(input("Selling_price:"))


def insert_data(item, buying, selling):
    cur.execute(
        "insert into products(name,buying_price,selling_price)values(%s, %s, %s)",
        (item, buying, selling),
    )
    conn.commit()
    print("Data Updated Successfully")


insert_data(item, buying, selling)