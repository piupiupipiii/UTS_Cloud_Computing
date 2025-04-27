import pymysql
from flask import Flask, render_template

app = Flask(__name__)

db = pymysql.connect(
    host='34.71.24.221',
    user='root',
    password='Pipi.123',
    database='products_db'
)

@app.route('/')
def home():
    cursor = db.cursor()
    cursor.execute('SELECT name, price, image_url FROM products')
    products = cursor.fetchall()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
