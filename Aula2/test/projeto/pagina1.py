from flask import Flask

app = Flask (__name__)

@app.route("/")
def index():
    return "Ola"

@app.route("/alunos")
def rota_aluno():
    return "Página dos alunos"

@app.route("/professores")
def rota_professores():
    return "Página dos professores"

@app.route("/notas")
def rota_notas():
    return "Página das notas"

@app.route("/coisas")
def rota_coisas():
    return "Página de coisas"

app.run()