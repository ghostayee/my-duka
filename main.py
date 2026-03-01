from flask import Flask, render_template, request, redirect, url_for
from database import (
    get_products,
    fetch_sales,
    insert_products,
    insert_sale,
    fetch_stock,
    insert_stock,
    available_stock,
    get_sales_per_day,
    get_profit_per_day,
    get_profit_per_product,
    get_sales_per_product,
)

# Flask instance
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/products")
def products():
    products = get_products()
    return render_template("products.html", products=products)


@app.route("/add_products", methods=["GET", "POST"])
def add_products():
    if request.method == "POST":
        product_name = request.form["p_name"]
        buying_price = request.form["b_price"]
        selling_price = request.form["s_price"]

        new_product = (product_name, buying_price, selling_price)
        insert_products(new_product)
        print("Product Added successfully")
    return redirect(url_for("products"))


@app.route("/sales")
def sales():
    products = get_products()
    sales = fetch_sales()
    return render_template("sales.html", products=products, sales=sales)


@app.route("/add_sales", methods=["GET", "POST"])
def add_sales():
    if request.method == "POST":
        product_id = request.form["products"]
        quantity = request.form["quantity"]

        new_sale = (product_id, quantity)
        check_stock = available_stock(product_id)
        if float(quantity) > check_stock:
            print("Insufficient stock,cant complete sale")
            return redirect
        insert_sale(new_sale)
        print("Sale Uploaded successfully")
    return redirect(url_for("sales"))


@app.route("/stock")
def stock():
    products = get_products()
    stock = fetch_stock()
    return render_template("stock.html", products=products, stock=stock)


@app.route("/insert_stock", methods=["GET", "POST"])
def insert_stocks():
    if request.method == "POST":
        product_id = request.form["product"]
        stock_quantity = request.form["stock"]

        new_stock = (product_id, stock_quantity)
        insert_stock(new_stock)
        print("Stock Updated successfully")
    return redirect(url_for("stock"))


@app.route("/dashboard")
def dashboard():
    sales_per_day = get_sales_per_day()
    profit_per_day = get_profit_per_day()
    sales_per_product = get_sales_per_product()
    profit_per_product = get_profit_per_product()

    day = [i[0] for i in sales_per_day]
    sales_day = [i[1] for i in sales_per_day]
    profit_day = [i[1] for i in profit_per_day]

    return render_template(
        "dashboard.html", day=day, sales_day=sales_day, profit_per_product=profit_per_product
    )


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


app.run(debug=True)
