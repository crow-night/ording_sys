from flask import Flask, render_template, request, session, flash, url_for, redirect
from model.demo.service import login_service

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

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
                return "The information you entered is wrong!"
        elif name in business:
            if business[name] == password:
                return render_template("businsess.html")
            else:
                return "The information you entered is wrong!"
        elif name in rider:
            if rider[name] == password:
                return  render_template("rider.html")
            else:
                return "The information you entered is wrong!"
        else:
            return "The information you entered is wrong!"

@app.route('/register_user', methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        phone = request.form.get("phone")
        password = request.form.get("password")
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        address = request.form.get("address")
        headPortrait = request.form.get("headPortrait")

        user, business, rider = login_service.login()
        if phone in user:
            return redirect(url_for("logins"))
        else:
            login_service.register((phone, password, name, age, gender, address, phone, headPortrait))
            return render_template("login.html")

    return render_template("register_user.html")

@app.route('/register_business', methods=["GET", "POST"])
def register_business():
    if request.method == "POST":
        phone = request.form.get("phone")
        password = request.form.get("password")
        name = request.form.get("name")
        address = request.form.get("address")
        headPortrait = request.form.get("headPortrait")

        user, business, rider = login_service.login()
        if phone in business:
            return redirect(url_for("logins"))
        else:
            login_service.register((phone, password, name, address, phone, headPortrait))
            return render_template("login.html")

    return render_template("register_business.html")

@app.route("/register_rider", methods=["GET", "POST"])
def register_rider():
    if request.method == "POST":
        phone = request.form.get("phone")
        password = request.form.get("password")
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        headPortrait = request.form.get("headPortrait")

        user, business, rider = login_service.login()
        if phone in rider:
            return redirect(url_for("logins"))
        else:
            login_service.register((phone, password, name, age, gender, phone, headPortrait))
            return render_template("login.html")

    return render_template("register_rider.html")

@app.route('/logins', methods=["GET", "POST"])
def logins():
    if request.method == "POST":
        pass
    return render_template("logins.html")

if __name__ == '__main__':
    app.run(debug=True)



