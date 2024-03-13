from flask import Flask, render_template, request

app = Flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calc")
def mostraCalc():
    return render_template("calc.html")

@app.route("/calcular_imc", methods=["POST"])
def calcIMC():
    altura = request.form["txt_altura"]
    peso = request.form["txt_peso"]


app.run()
