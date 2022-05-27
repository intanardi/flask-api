from flask import Flask, request
from app.models import User, Order
import time
import timeit
from datetime import datetime, timedelta


app = Flask(__name__)


@app.route("/login", methods=['POST'])
def login():
    print("login")
    date_log =datetime.now()
    start_time = datetime.now()
    status = "login failed username or password is wrong"
    username = request.json['username']
    password = request.json['password']
    check = User().login(username, password)
    if check:
        status = "login success"
    end_time = datetime.now()
    interval = end_time - start_time
    print_response = '{} : Login process done in {} seconds\n'.format(date_log, interval)
    print(print_response)
    f = open("flask_speed_log.txt", "a")
    f.write(print_response)
    f.close()
    return status

@app.route("/getAllOrder", methods=['GET'])
def get_all():
    print("get all data")
    date_log = datetime.now()
    start_time = datetime.now()
    response = Order().getAllOrder()
    end_time = datetime.now()
    interval = end_time - start_time
    print_response = '{} : Get All Order process done in {} seconds\n'.format(date_log, interval)
    print(print_response)
    f = open("flask_speed_log.txt", "a")
    f.write(print_response)
    f.close()
    return response

@app.route("/getProductOrder", methods=['POST'])
def get_product_by_id():
    print("get prod data")
    date_log = datetime.now()
    start_time = datetime.now()
    order_id = request.json['id']
    response = Order().getOrdertById(order_id)
    end_time = datetime.now()
    interval = end_time - start_time
    print_response = '{} : Get Product Order process done in {} seconds\n'.format(date_log, interval)
    print(print_response)
    f = open("flask_speed_log.txt", "a")
    f.write(print_response)
    f.close()
    return response

if __name__ == "__main__":
    app.run(debug=True)