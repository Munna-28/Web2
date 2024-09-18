from flask import Flask,render_template,redirect,url_for,session,request
from datetime import tiedelta
app.permanent_session_lifetime = timedelta(minuters=5)
app=Flask(__name__)
app.secret_key="hero"

@app.route("/")
def home() :
    return render_template("n.html")

@app.route("/<name>")
def user(name):
    return f"Hey! how are you {name}?"

@app.route("/login",methods=["POST","GET"])
def login():
     if request.method=="POST":
        session.permentant=True
        user=request.form["nm"]
        session["user"]=user
        return redirect(url_for("user",name=user))
     else:
          return render_template("login.html")


if __name__=="__main__":
    app.run(debug=True)