from flask import Flask, render_template, redirect, url_for, session, request
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hero"
app.permanent_session_lifetime = timedelta(minutes=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


@app.route("/")
def home():
    return render_template("blog.html")

@app.route("/sample")
def sample():
    return render_template("sample.html")

@app.route("/cv")
def cv():
    return render_template("cv.html")

@app.route("/contact")
def contact():
    return render_template("n.html")

@app.route("/<name>")
def user(name):
    return f"Thank you {name}! Have a nice day :)"

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        found_user = Users.query.filter_by(name=user).first()
        if found_user:
            session["name"] = found_user.name
        else:
            new_user = Users(name=user)
            db.session.add(new_user)
            db.session.commit()
        return redirect(url_for("user", name=user))
    else:
        return render_template("login.html")

@app.route("/admin-Nikhil")
def view():
    return render_template("view.html", values=Users.query.all())

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
