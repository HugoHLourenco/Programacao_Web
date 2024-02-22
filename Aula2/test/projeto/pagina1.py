from flask import Flask

app = Flask (__name__)

@app.route("/")
def index():
    return "<h1>Ola</h1>" \
        "<img src = 'https://picsum.photos/600/600'>"

@app.route("/alunos")
def rota_aluno():
    return "<p>Página dos alunos</p>" \
        "<img src = 'https://picsum.photos/600/600'>"

@app.route("/professores")
def rota_professores():
    return "<h1>Página dos professores</h1>" \
        "<p>Olha a tag HTML de paragrafo aqui</p>" \
        "<img src = 'https://picsum.photos/600/600'>"

@app.route("/notas")
def rota_notas():
    return "<p>Página das notas</p>" \
        "<img src = 'https://picsum.photos/600/600'>"

@app.route("/coisas")
def rota_coisas():
    return "<p>Página de coisas</p>" \
        "<img src = 'https://picsum.photos/600/600'>"

app.run()