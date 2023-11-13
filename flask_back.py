from flask import Flask, render_template, url_for, redirect, request, session, flash
# time to token expire
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=0.2)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash(f"Login succesfull, {user}", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash(f"Aldready logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods=["GET"])
def user():
    if "user" in session:
        user = session["user"]
        flash(f"You are not logged in!")
        return render_template("user.html", user=user)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash(f"Logout sucessfull")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)
