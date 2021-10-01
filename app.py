from flask.helpers import url_for
from extensions import app, db, render_template, redirect

list_chapter=['Programming','Sport','Traiding']


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

@app.route("/library")
def library():
    return render_template('programming/library.html')       

@app.route("/content1")
def content1():
    return render_template('programming/content1.html')

@app.route("/resources")
def resources():
    return render_template('programming/resources.html')

if __name__=="__main__":
    app.run(debug=True)

     