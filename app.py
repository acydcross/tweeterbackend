import mariadb
from flask import Flask, request, Response
import json
import dbcreds
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/login', methods=['POST', 'DELETE'])
def user():
    if request.method == 'POST':
        conn = None
        cursor = None
        user = None
        rows = None
        user_email = request.json.get('email')
        user_password = request.json.get('password')
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user WHERE email = ? AND password = ?", [user_email, user_password])
            user = cursor.fetchall()
            rows = cursor.rowcount
            print (user[0][0])
        except Exception as error:
            print("Something went wrong (THIS IS LAZY): ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(user != None):
                return Response(json.dumps(user, default=str), mimetype="application/json", status=200)
            else:
                return Response("Something went wrong!", mimetype="text/html", status=500)
    elif request.method == 'DELETE':
        conn = None
        cursor = None
        rows = None

@app.route('/api/login', methods=['POST', 'DELETE'])
def login():