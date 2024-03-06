from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def mostraAbout():
    return render_template("about.html")

@app.route("/contact")
def mostraContact():
    return render_template("contact.html")

@app.route("/services")
def mostraServices():
    return render_template("services.html")

app.run()