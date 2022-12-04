from flask import Flask, url_for, redirect, render_template, request
from flask_mysqldb import MySQL
import hashlib

app = Flask(__name__)

app.config["MYSQL_HOST"] = "Sanel.mysql.pythonanywhere-services.com"
app.config["MYSQL_USER"] = "Sanel"
app.config["MYSQL_PASSWORD"] = "costisolCatalizer"
app.config["MQSQL_DB"] = "Sanel$users"
TABLE_NAME = "Sanel$users"

db = MySQL(app)
conn = db

def login(email, password):
    if db.connection.errno():
        return "4"

    cursor = db.connection.cursor()

    email_check_query = f'SELECT email, hash, salt, firstName from {TABLE_NAME} where email="{email}";'

    if cursor.rowcount == 1:

        details = cursor.fetchall()[0]

        salt = details[2]
        db_hash = details[1]
        password_hash = sha512(password, salt)

        if db_hash == password_hash:
            cursor.close()
            return render_template("home.html")
        cursor.close()
        return "2"
    else:
        cursor.close()
        return "3"

def definePages():
    @app.route("/login/", methods=["POST", "GET"])
    @app.route("/login/<e>", methods=["POST", "GET"])
    def login_page(e=""):
        text = e
        if e == "3" or e == "2":
            text = "Wrong email or password"
        if e == "4":
            text = "Internal server error"
        return render_template("login.html", text=text)

    @app.route("/", methods=["POST", "GET"])
    def home_page():
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            return login(email, password)
        elif request.method == "GET":
            return redirect(url_for("login_page"))

def sha512(string, salt):
    return hashlib.sha512((string + salt).encode()).hexdigest()

if __name__ == "__main__":
    definePages()
    app.run(debug=True)