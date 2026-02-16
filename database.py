import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="Ford6000$$$...",
    dbname="myduka_db",
)


cur = conn.cursor()

"""def get_data(table):
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


insert_data(item, buying, selling)"""

# task on get data from the sales table and products.
pid = int(input("ProductID:"))
quantity = int(input("Enter number sold:"))


def sales_made():
    cur.execute(f"insert into sales(pid,quantity)values({pid},{quantity})")
    conn.commit()
    print("sales successfully recorded")


# sales_made()


def sales():
    cur.execute("select * from sales")
    data = cur.fetchall()
    print(data)


print("\nSALES PER PRODUCT")
cur.execute(
    """
SELECT p.name,
    SUM(s.quantity) AS total_quantity_sold
FROM sales s
JOIN products p ON s.pid = p.id
GROUP BY p.name
"""
)

for row in cur.fetchall():
    print(f"Product: {row[0]}, Total Sold: {row[1]}")


# Sales per day
print("\nSALES PER DAY")
cur.execute(
    """
SELECT DATE(s.created_at) AS sale_date,
    SUM(s.quantity) AS total_quantity_sold
FROM sales s
GROUP BY DATE(s.created_at)
ORDER BY sale_date
"""
)

for row in cur.fetchall():
    print(f"Date: {row[0]}, Total Sold: {row[1]}")


# Profit per product
print("\nPROFIT PER PRODUCT")
cur.execute(
    """
SELECT p.name,
       SUM((p.selling_price - p.buying_price) * s.quantity) AS total_profit
FROM sales s
JOIN products p ON s.pid = p.id
GROUP BY p.name
"""
)

for row in cur.fetchall():
    print(f"Product: {row[0]}, Profit: {row[1]}")


# Profit per day
print("\nPROFIT PER DAY")
cur.execute(
    """
SELECT DATE(s.created_at) AS sale_date,
       SUM((p.selling_price - p.buying_price) * s.quantity) AS total_profit
FROM sales s
JOIN products p ON s.pid = p.id
GROUP BY DATE(s.created_at)
ORDER BY sale_date
"""
)

for row in cur.fetchall():
    print(f"Date: {row[0]}, Profit: {row[1]}")

#necessary for this
#==>
#==>
#cur.close()
#conn.close()
