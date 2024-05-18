from flask import Flask, request, render_template, redirect, url_for
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

## pg cadastro
@app.route("/cadastro")
def mostraCadastro():
    return render_template("cadastro.html")

@app.route("/cadastro_usuario", methods =['POST'])
def cadastro():
    nome = request.form['txt_nome']
    cpf = request.form['txt_cpf']
    email = request.form['txt_email']
    senha = request.form['txt_senha']
    db = mysql.connector.connect(host = '201.23.3.86', 
                                 port= 5000,
                                 user= 'usr_aluno',
                                 password= 'E$tud@_m@1$',
                                 database= 'aula_fatec')
    mycursor = db.cursor()
    query = 'INSERT INTO Hugo_IIItbusuario ( nome, cpf, email, senha) VALUES (%s, %s, %s, %s)'
    values = (nome, cpf, email, senha)
    mycursor.execute(query, values)
    db.commit()
    return render_template("gravou.html")

# mostra tabela
@app.route("/caduser")
def lista_user():
    db = mysql.connector.connect(host = '201.23.3.86',
                                 port = 5000,
                                 user = 'usr_aluno',
                                 password= 'E$tud@_m@1$',
                                 database= 'aula_fatec')
    mycursor = db.cursor()
    query = 'select nome, cpf, email, id from Hugo_IIItbusuario'
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('caduser.html', opcao = 'listar' ,usuarios = resultado)

# 
@app.route("/alternar_usuario/<user>")
def alternar_usuario(user):
    db = mysql.connector.connect(host = '201.23.3.86',
                                 port = 5000,
                                 user = 'usr_aluno',
                                 password= 'E$tud@_m@1$',
                                 database= 'aula_fatec')
    mycursor = db.cursor()
    query = 'select nome, cpf, email from Hugo_IIItbusuario where id = ' + user
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('cadastro.html', opcao = 'alterar', usuarios = resultado)

@app.route("/update_usuario", methods = ["POST"])
def update_usuario():
    nome = request.form["txt_nome"]
    cpf = request.form["txt_cpf"]
    email = request.form["txt_email"]
    senha = request.form["txt_senha"]
    id = request.form["txt_id"]
    db = mysql.connector.connect(host = '201.23.3.86',
                                 port = 5000,
                                 user = 'usr_aluno',
                                 password= 'E$tud@_m@1$',
                                 database= 'aula_fatec')
    mycursor = db.cursor()
    query = "update Hugo_IIItbusuario set nome = '" + nome + "', cpf = '" + cpf + "', email = '" + email + "', senha = '" + senha + "' where id = " + id
    mycursor.execute(query)
    db.commit()
    return redirect("/caduser")
##

@app.route("/exclui_usuario/<user>")
def exclui_usuario(user):
    db = mysql.connector.connect(host = '201.23.3.86',
                                 port = 5000,
                                 user = 'usr_aluno',
                                 password= 'E$tud@_m@1$',
                                 database= 'aula_fatec')
    mycursor = db.cursor()
    query = "delete from Hugo_IIItbusuario where id = " + user 
    mycursor.execute(query)
    db.commit()
    mycursor.close()
    db.close()
    return render_template("deletou.html") 






## Pg que mostra o cadastro de cliente
@app.route('/cadastrocliente')
def mostraCadastroCliente():
    return render_template('/cadastrocliente.html')
## Método de cadastro de cliente
@app.route('/cadastro_cliente', methods =['POST'])
def cadastroCliente():
    nome = request.form['txt_nome']
    datanasc = request.form['txt_datanasc']
    cpf = request.form['txt_cpf']
    rg = request.form['txt_rg']
    email = request.form['txt_email']
    endereco = request.form['txt_endereco']
    bairro = request.form['txt_bairro']
    cidade = request.form['txt_cidade']
    uf = request.form['txt_uf']
    cep = request.form['txt_cep']
    db = mysql.connector.connect(host = '201.23.3.86', 
                                 port= 5000,
                                 user= 'usr_aluno',
                                 password= 'E$tud@_m@1$',
                                 database= 'aula_fatec')
    mycursor = db.cursor()
    query = 'INSERT INTO Hugo_tbcliente ( nome, datanasc, cpf, rg, email, endereco, bairro, cidade, uf, cep) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    values = (nome, datanasc, cpf, rg, email, endereco, bairro, cidade, uf, cep)
    mycursor.execute(query, values)
    db.commit()
    return render_template('/cadastrocliente.html')

## Mostra a tabela cliente
@app.route("/tabelacliente")
def tabelaDoCliente():
    db = mysql.connector.connect(host = '201.23.3.86',
                                 port = 5000,
                                 user = 'usr_aluno',
                                 password= 'E$tud@_m@1$',
                                 database= 'aula_fatec')
    mycursor = db.cursor()
    query = 'select nome, datanasc, cpf, rg, email, endereco, bairro, cidade, uf, cep from Hugo_tbcliente'
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('/tabelacliente.html', opcao = 'listar' , clientes = resultado)

## Faz o update da tabela -------------------------------------------------------
@app.route("/update_cliente", methods = ["POST"])
def update_cliente():
    nome = request.form['txt_nome']
    datanasc = request.form['txt_datanasc']
    cpf = request.form['txt_cpf']
    rg = request.form['txt_rg']
    email = request.form['txt_email']
    endereco = request.form['txt_endereco']
    bairro = request.form['txt_bairro']
    cidade = request.form['txt_cidade']
    uf = request.form['txt_uf']
    cep = request.form['txt_cep']
    id = request.form["txt_id"]
    db = mysql.connector.connect(host = '201.23.3.86',
                                 port = 5000,
                                 user = 'usr_aluno',
                                 password= 'E$tud@_m@1$',
                                 database= 'aula_fatec')
    mycursor = db.cursor()
    query = "update Hugo_tbcliente set nome = '" + nome + "', datanasc = '" + datanasc + "', cpf = '" + cpf + "', rg = '" + rg + "', email = '" + email + "', endereco = '" + endereco + "', bairro = '" + bairro + "', cidade =  '" + cidade + "', uf = '" + uf + "', cep = '" + cep + "' where id = " + id
    mycursor.execute(query)
    db.commit()
    return redirect("/tabelacliente")

@app.route("/alternar_cliente/<user>")
def alternar_cliente(user):
    db = mysql.connector.connect(host = '201.23.3.86',
                                 port = 5000,
                                 user = 'usr_aluno',
                                 password= 'E$tud@_m@1$',
                                 database= 'aula_fatec')
    mycursor = db.cursor()
    query = 'select nome, datanasc, cpf, rg, email, endereco, bairro, cidade, uf, cep from Hugo_tbcliente where id = ' + user
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('cadastrocliente.html', opcao = 'alterar', clientes = resultado)
## -------------------------------------------------------------------------------
## Exclusão ----------------------------------------------------------------------
@app.route("/exclui_cliente/<user>", methods=['POST'])
def exclui_cliente(user):
    db = mysql.connector.connect(host = '201.23.3.86',
                                 port = 5000,
                                 user = 'usr_aluno',
                                 password= 'E$tud@_m@1$',
                                 database= 'aula_fatec')
    mycursor = db.cursor()
    query = "delete from Hugo_tbcliente where id = " + user 
    mycursor.execute(query)
    db.commit()
    mycursor.close()
    db.close()
    return redirect(url_for('tabelacliente'))


# @app.route("/exclui_usuario/<user>")
# def exclui_usuario(user):
#     db = mysql.connector.connect(host = '201.23.3.86',
#                                  port = 5000,
#                                  user = 'usr_aluno',
#                                  password= 'E$tud@_m@1$',
#                                  database= 'aula_fatec')
#     mycursor = db.cursor()
#     query = "delete from Hugo_IIItbusuario where id = " + user 
#     mycursor.execute(query)
#     db.commit()
#     mycursor.close()
#     db.close()
#     return render_template("deletou.html")

app.run()
