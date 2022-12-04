from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "Sanel.mysql.pythonanywhere-services.com"
app.config["MYSQL_USER"] = "Sanel"
app.config["MYSQL_PASSWORD"] = "10562ltufekcic"
app.config["MQSQL_DB"] = "Sanel$patients"
TABLE_NAME = "patients"

db = MySQL(app)
conn = db

mycursor=db.cursor()

mycursor.execute("SELECT patients.first_name,patients.last_name, patients.date, patients.c_time FROM patients, users WHERE patients.dr_id=users.dr_id")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)