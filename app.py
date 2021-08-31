from flask import Flask, render_template, request, session, flash, url_for, redirect
from model.db.service import login_service
from model.db.riders import riders_dao
from model.db.users import users_dao
from model.db.business import business_dao

app = Flask(__name__)

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
                return render_template("users.html")
            else:
                return "The information you entered is wrong1!"
        elif name in business:
            if business[name] == password:
                return render_template("business.html")
            else:
                return "The information you entered is wrong2!"
        elif name in rider:
            if rider[name] == password:
                return render_template("rider.html")
            else:
                return "The information you entered is wrong3!"
        else:
            return "The information you entered is wrong4!"



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
                return render_template("index.html")
            else:
                login_service.users_dao.insert_users((account, password, name, age, gender, address, phone, headPortait))
                print(name, account, password, phone, age, gender, address,headPortait)
                return render_template("users.html")

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
                login_service.business_dao.insert_business((account, password, name, address, phone, headPortait))
                return render_template("business.html")

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
                login_service.riders_dao.insert_riders((account, password, name, age, gender,  phone, headPortait))
                return render_template("rider.html")
    return render_template("register.html")


@app.route('/logins', methods=["GET", "POST"])
def logins():
    if request.method == "POST":
        pass
    return render_template("logins.html")

@app.route('/rider_profile', methods=["GET"])
def get_riders():
    account = "r"
    data = riders_dao.get_riders_one(account)

    return render_template("rider/profile.html", **data)

@app.route('/user_profile', methods=["GET"])
def get_users():
    account = "night_crow"
    data = users_dao.get_users_one(account)

    return render_template("user/profile.html", **data)


@app.route('/business_profile', methods=["GET"])
def get_business():
    account = "b"
    data = business_dao.get_business_one(account)

    return render_template("business/profile.html", **data)

@app.route('/modify_user_password', methods=["GET"])
def modify_user_password():
    account = request.form["account"]

    newpassword = request.form.get("Passwords")
    users_dao.modify_password((newpassword, account))

    data = users_dao.get_users_one(account)
    return render_template("user/profile.html", **data)


if __name__ == '__main__':
    app.run(debug=True)



