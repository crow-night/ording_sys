from flask import Flask, render_template, request, session, flash, url_for, redirect
from model.db.service import login_service
from model.db.riders import riders_dao
from model.db.users import users_dao
from model.db.business import business_dao
from model.db.dishes import  dishes_dao
from datetime import timedelta
from model.db.order import userorder_dao, businessorder_dao, riderorder_dao

app = Flask(__name__)
account_data = {"user":None, "business":None, "rider":None}
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")

        user, business, rider = login_service.login()
        if name in user:
            if user[name] == password:
                account_data["user"] = name
                # data = users_dao.get_users_one(name)
                # return render_template("users.html", **data)

                data = dishes_dao.find_all()
                # account = account_data["user]
                # accounts = users_dao.get_users_one(account)
                # return render_template("user/dishes.html", data=data, **accounts)
                return render_template("user/dishes.html", data=data)
            else:
                return render_template("login.html")
        elif name in business:
            if business[name] == password:
                account_data["business"] = name
                # data = business_dao.get_business_one(name)
                # return render_template("business.html", **data)

                data = dishes_dao.find_all()
                return render_template("business/dishes.html", data=data)
            else:
                return render_template("login.html")
        elif name in rider:
            if rider[name] == password:
                account_data["rider"]=name
                # data = riders_dao.get_riders_one(name)
                # return render_template("rider.html", **data)

                data_complete = riderorder_dao.find_complete()
                data_incomplete = riderorder_dao.find_incomplete()
                return render_template('rider/orders.html', data_complete=data_complete, data_incomplete=data_incomplete)
            else:
                 return render_template("login.html")
        else:
            return render_template("login.html")

@app.route('/logins', methods=["GET", "POST"])
def logins():
    if request.method == "POST":
        return render_template('index.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        choose = request.values.get("choose")
        if choose == "users":
            name = request.form.get("name")
            account = request.form.get("account")
            password = request.form.get("pwd")
            phone = request.form.get("tpe")
            age = request.form.get("age")
            gender = request.form.get("gender")
            address = request.form.get("address")
            # headPortrait = request.form.get("headPortrait")
            headPortait = None

            user, business, rider = login_service.login()
            if account in user:
                render_template("index.html")
            else:
                account_data["user"] = account
                login_service.users_dao.insert_users((account, password, name, age, gender, address, phone, headPortait))
                data = dishes_dao.find_all()
                return render_template("user/dishes.html", data=data)

        elif choose == "business":
            name = request.form.get("name")
            account = request.form.get("account")
            password = request.form.get("pwd")
            phone = request.form.get("tpe")
            age = request.form.get("age")
            gender = request.form.get("gender")
            address = request.form.get("address")
            headPortait = None

            user, business, rider = login_service.login()
            if account in business:
                return render_template("index.html")
            else:
                account_data["business"] = account
                login_service.business_dao.insert_business((account, password, name, address, phone, headPortait))
                data = dishes_dao.find_all()
                return render_template("business/dishes.html", data=data)

        else:
            name = request.form.get("name")
            account = request.form.get("account")
            password = request.form.get("pwd")
            phone = request.form.get("tpe")
            age = request.form.get("age")
            gender = request.form.get("gender")
            headPortait = None

            user, business, rider = login_service.login()
            if account in rider:
                return render_template("index.html")
            else:
                account["rider"] = account
                login_service.riders_dao.insert_riders((account, password, name, age, gender,  phone, headPortait))
                data_complete = riderorder_dao.find_complete()
                data_incomplete = riderorder_dao.find_incomplete()
                return render_template('rider/orders.html', data_complete=data_complete,data_incomplete=data_incomplete)

    return render_template("register.html")


@app.route('/out', methods=["GET"])
def out():
    render_template("index.html")


@app.route('/user_dishes', methods=["GET"])
def user_dishes():
    data = dishes_dao.find_all()
    return render_template("user/dishes.html", data=data)

@app.route('/user_profile', methods=["GET"])
def user_profile():
    # account = account_data[0]
    account = account_data["user"]
    data = users_dao.get_users_one(account)
    return render_template("user/profile.html", **data)

@app.route('/user_shopping', methods=["POST"])
def user_shopping():
    pass

@app.route('/user_order', methods=["GET", "POST"])
def user_order():
    data_complete = userorder_dao.find_complete()
    data_incomplete = userorder_dao.find_incomplete()
    return render_template("user/orders.html", data_complete=data_complete, data_incomplete=data_incomplete)

@app.route('/business_dishes', methods=["GET"])
def business_dishes():
    data = dishes_dao.find_all()
    return render_template("business/dishes.html", data=data)

@app.route('/business_profile', methods=["GET"])
def business_profile():
    account = account_data["business"]
    data = business_dao.get_business_one(account)
    return render_template("business/profile.html", **data)

@app.route('/business_order', methods=["GET"])
def business_order():
    data_complete = businessorder_dao.find_complete()
    data_incomplete = businessorder_dao.find_incomplete()
    return render_template("business/orders.html", data_complete=data_complete, data_incomplete=data_incomplete)

@app.route('/rider_order', methods=["GET"])
def rider_order():
    data_complete = riderorder_dao.find_complete()
    data_incomplete = riderorder_dao.find_incomplete()
    return render_template('rider/orders.html', data_complete=data_complete, data_incomplete=data_incomplete)

@app.route('/rider_profile', methods=["GET"])
def rider_profile():
    # account = account_data[0]
    account = account_data["rider"]
    data = riders_dao.get_riders_one(account)
    return render_template("rider/profile.html", **data)

# @app.route('/modify_user_password', methods=["GET"])
# def modify_user_password():
#     account = request.form["account"]
#
#     newpassword = request.form.get("Passwords")
#     users_dao.modify_password((newpassword, account))
#
#     data = users_dao.get_users_one(account)
#     return render_template("user/profile.html", **data)

#取消缓存
app.config["SEND_FILE_MAX_AGE_DEFAULT"] =timedelta(seconds=1)


if __name__ == '__main__':
    app.run(debug=True)




