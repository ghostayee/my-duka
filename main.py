from flask import Flask,render_template
from database import get_products,fetch_sales

#Flask instance
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/products')
def products():
    products = get_products()
    return render_template('products.html',products =products)



@app.route('/sales')
def sales():
    sales = fetch_sales()
    return render_template('sales.html',sales = sales)



@app.route('/stock')
def stock():
    value = 789
    numbers = [1,2,3,4,5,6,7,8,9]
    return render_template('stock.html',x = value,y=numbers)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')




app.run(debug=True)