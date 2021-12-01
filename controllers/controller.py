from app import app
from flask import render_template
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html' , title="My order", orders=orders)

@app.route('/orders/<index>')
