from flask import Flask, render_template
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host='IP_DATABASE',
    user='root',
    password='PASSWORD',
    database='products_db'
)

@app.route('/')
def home():
    cursor = db.cursor()
    cursor.execute('SELECT name, price, image_url FROM products')
    products = cursor.fetchall()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
