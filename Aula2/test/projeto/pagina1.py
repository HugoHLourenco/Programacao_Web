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
    return "<h1>Página dos professores</h1>" \
        "<p>Olha a tag HTML de paragrafo aqui</p>" \
        "<img src = 'https://picsum.photos/600/600'>"

@app.route("/notas")
def rota_notas():
    return "Página das notas"

@app.route("/coisas")
def rota_coisas():
    return "Página de coisas"

app.run()