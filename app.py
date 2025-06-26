from flask import Flask, render_template, request, redirect
import pymysql
import os

app = Flask(__name__)

# Database connection config
DB_HOST = os.environ.get("DB_HOST", "34.47.235.229")
DB_USER = os.environ.get("DB_USER", "libuser")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "libpass")
DB_NAME = os.environ.get("DB_NAME", "library")

# Connect to database
conn = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    db=DB_NAME,
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def index():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
        conn.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
