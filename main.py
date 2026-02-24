from flask import Flask, render_template
from database import get_products, fetch_sales


app = Flask(__name__)


app.run(debug=True)
