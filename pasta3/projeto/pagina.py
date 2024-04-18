from flask import Flask, request, render_template
import mysql.connector

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

@app.route("/cadastro")
def mostraCadastro():
    return render_template("cadastro.html")


@app.route("/cadastro", methods =['POST'])
def cadastro():
    nome = request.form['txt_nome']
    cpf = request.form['txt_cpf']
    email = request.form['txt_email']
    senha = request.form['txt_senha']
    db = mysql.connector.connect(host = '201.23.3.86', 
                                 port= 5000,
                                 user= "usr_aluno",
                                 password= "E$tud@_m@1$",
                                 database= "aula_fatec")
    mycursor = db.cursor()
    query = "INSERT INTO HugoIII_tbusuario ( nome, cpf, email, senha) VALUES (%s, %s, %s, %s)"
    values = (nome,cpf,email, senha)
    mycursor.execute(query, values)
    db.commit()
    return "gravou"
    
app.run()
