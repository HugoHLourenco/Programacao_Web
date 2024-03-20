from flask import Flask, render_template, request

app = Flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calc")
def mostraCalc():
    return render_template("calc.html")

#post
@app.route("/calcular_imc", methods=["POST"])
def calcIMC():
    altura = float(request.form["txt_altura"])
    peso = float(request.form["txt_peso"])
    imc = peso / (altura * altura)
    if (imc < 18.5):
        classificacao = "IMC magro"
    if(imc >= 18.5 and imc <= 24.9):
        classificacao = "IMC normal"
    if(imc >=25 and imc <= 29.9):
        classificacao = "IMC sobrepeso"
    if(imc >= 30 and imc <= 39.9):
        classificacao = "IMC de obesidade"
    if (imc >= 40):
        classificacao = "IMC de obesidade grave"
    return render_template("calc.html", res_imc =f'{imc:.2f}', res_classificacao = classificacao)

#get
@app.route("/calcular_imc_get")
def calc_imc_get():
    args = request.args
    altura = float(args.get("txt_altura"))
    peso = float(args.get("txt_peso"))
    imc = peso / (altura * altura)
    if (imc < 18.5):
        classificacao = "IMC magro"
    if(imc >= 18.5 and imc <= 24.9):
        classificacao = "IMC normal"
    if(imc >=25 and imc <= 29.9):
        classificacao = "IMC sobrepeso"
    if(imc >= 30 and imc <= 39.9):
        classificacao = "IMC de obesidade"
    if (imc >= 40):
        classificacao = "IMC de obesidade grave"
    return render_template("calc.html", res_imc =f'{imc:.2f}', res_classificacao = classificacao)

app.run()
