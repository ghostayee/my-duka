import psycopg2

# establishes a new db connection
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="Ford6000$$$...",
    dbname="myduka_db",
)

# cursor object
cur = conn.cursor()


def get_data(table):
    cur.execute(f"select * from {table}")
    data = cur.fetchall()
    return data


# data = get_data("sales")
# print(data)


def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products


# products = get_products()
# print(products)


def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()


product1 = ("samsung", 20000, 30000)
product2 = ("hp", 30000, 40000)

# insert_products(product1)
# insert_products(product2)


def fetch_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales


# sales = fetch_sales()
# print(sales)


def insert_sale(values):
    cur.execute(f"insert into sales(pid,quantity)values{values}")
    conn.commit()


sale1 = (12, 30)
sale2 = (14, 12)

# insert_sale(sale1)
# insert_sale(sale2)

# print(sales1)


def fetch_stock():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock


# stock = fetch_stock()
# print(stock)


def get_stock():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock


# stock_data = get_stock()
# print("this is stock", stock_data)


def insert_stock(values):
    cur.execute(f"insert into stock(pid,stock_quantity)values{values}")
    conn.commit()


stock1 = (13, 90)
stock2 = (15, 60)
# insert_stock(stock1)


def get_sales_per_product():
    cur.execute(
        """
        select products.name as p_name , sum(products.selling_price * sales.quantity) as total_sales
        from products join sales on sales.pid = products.id group by(p_name);
    """
    )
    sales_per_product = cur.fetchall()
    return sales_per_product


# sales_per_product = get_sales_per_product()
# print(sales_per_product)


def get_profit_per_day():
    cur.execute(
        """
        select date(sales.created_at) as date , sum((products.selling_price - products.buying_price)
     * sales.quantity) as profit from sales join products on products.id = sales.pid group by(date);
    """
    )
    profit_per_day = cur.fetchall()
    return profit_per_day


# profit_per_day = get_profit_per_day()
# print(profit_per_day)


def get_sales_per_day():
    cur.execute(
        """
        select date(sales.created_at) as day ,sum(sales.quantity * products.selling_price) t_sales from sales join
         products on products.id = sales.pid group by(day)
    """
    )
    sales_per_day = cur.fetchall()
    return sales_per_day


sales_per_day = get_sales_per_day()
print(sales_per_day)


def get_profit_per_product():
    cur.execute(
        """
        select products.name as p_name , sum((products.selling_price - products.buying_price) * sales.quantity) as profit
                from sales join products on products.id = sales.pid group by p_name
    """
    )
    profit_per_product = cur.fetchall()
    return profit_per_product


profit_per_product = get_profit_per_product()
print(profit_per_product)


def available_stock(pid):
    cur.execute("select sum(stock_quantity) from stock where pid = %s", (pid,))
    total_stock = cur.fetchone()[0] or 0

    cur.execute("select sum(quantity) from sales where pid = %s", (pid,))
    total_sold = cur.fetchone()[0] or 0

    return total_stock - total_sold

def create_user("full_name,email,phone_number,password)values(%s,%s,%s,%s)" values)



def check_user(email):
    cur.execute("select * from users where email = %s",(email,))
    user_data = cur.fetchone()
    return user_data