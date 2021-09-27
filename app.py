from flask.helpers import url_for
from extensions import app, db, render_template, redirect

@app.route("/")
def index():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')    

if __name__=="__main__":
    app.run(debug=True)