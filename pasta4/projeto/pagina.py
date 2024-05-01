from flask import Flask, render_template, request
import mysql.connector

app = Flask (__name__)
@app.route("/")
def raiz():
    return render_template('cadusuario.html')

@app.route('/cadastrar_usuario',methods=['POST'])
def inserir_usuario():
    nome = request.form['txt_nome']
    cpf = request.form['txt_cpf']
    email = request.form['txt_email']
    senha = request.form['txt_senha']
    db = mysql.connector.connect(host='201.23.3.86', port=5000, user='usr_aluno',password='E$tud@_m@1$',database='aula_fatec')
    mycursor = db.cursor()
    query = "INSERT INTO Hugo_IIItbusuario (nome, cpf, email, senha) VALUES (%s,%s,%s,%s)"
    values = (nome, cpf, email, senha)
    mycursor.execute(query,values)
    db.commit()
    return 'gravou'

@app.route('/usercad')
def lista_user():
    db = mysql.connector.connect(host='201.23.3.86',
                                port=5000,
                                user='usr_aluno',
                                password='E$tud@_m@1$',
                                database='aula_fatec')
    mycursor = db.cursor()
    query = 'select nome, cpf, email from Hugo_IIItbusuario'
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('cadusuario.html', opcao='listar', usuarios= resultado)

@app.route('/alterar_usuario/<user>') #Carregar a página de cadastro
def alterar_usuario(user):
    db = mysql.connector.connect(host='201.23.3.86',
                                port=5000,
                                user='usr_aluno',
                                password='E$tud@_m@1$',
                                database='aula_fatec')
    mycursor = db.cursor()
    query = 'select nome, cpf, email, id from Hugo_IIItbusuario where id = ' + user
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('cadusuario.html', usuarios= resultado)

app.run()