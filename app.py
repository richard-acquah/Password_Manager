from flask import Flask, render_template, request, redirect, url_for, flash
from cryptography.fernet import Fernet
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

# Load or generate encryption key
def load_or_create_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key

# Encrypt password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Decrypt password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Initialize database
def init_db():
    with sqlite3.connect("passwords.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                username TEXT NOT NULL,
                password BLOB NOT NULL
            )
        """)
        conn.commit()

# Store password in the database
def store_password(service, username, encrypted_password):
    with sqlite3.connect("passwords.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)", 
                       (service, username, encrypted_password))
        conn.commit()

# Retrieve password from the database
def retrieve_passwd(service):
    with sqlite3.connect("passwords.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT username, password FROM passwords WHERE service = ?", (service,))
        return cursor.fetchone()

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_passwd():
    if request.method == 'POST':
        service = request.form['service']
        username = request.form['username']
        password = request.form['password']
        key = load_or_create_key()
        encrypted_password = encrypt_password(password, key)
        store_password(service, username, encrypted_password)
        flash("Password stored successfully!")
        return redirect(url_for('index'))
    return render_template('add_passwd.html')

@app.route('/retrieve', methods=['GET', 'POST'])
def retrieve():
    if request.method == 'POST':
        service = request.form['service']
        key = load_or_create_key()
        result = retrieve_passwd(service)
        if result:
            username, encrypted_password = result
            password = decrypt_password(encrypted_password, key)
            return render_template('retrieve_passwd.html', service=service, username=username, password=password)
        else:
            flash("No password found for that service.")
            return redirect(url_for('retrieve'))
    return render_template('retrieve_passwd.html', service=None, username=None, password=None)

if __name__ == '__main__':
    init_db()  # Initialize the database if it doesn't exist
    app.run(debug=True)
