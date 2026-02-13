import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="Ford6000$$$...",
    dbname="my_duka",
)

cur = conn.cursor()

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
