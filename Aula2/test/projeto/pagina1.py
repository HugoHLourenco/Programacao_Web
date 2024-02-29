from flask import Flask, render_template

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

@app.route("/template")
def mostraTemplepate():
    return render_template("minhapagina.html")

@app.route("/pag2")
def mostrapag2():
    return render_template("pag2.html")

@app.route("/pag3")
def mostrapag3():
    return render_template("pag3.html")

@app.route("/pag4")
def mostrapag4():
    return render_template("pag4.html")

@app.route("/index")
def mostraindex():
    return render_template("index.html")

@app.route("/about")
def mostraabout():
    return render_template("about.html")

@app.route("/contact")
def mostracontact():
    return render_template("contact.html")

@app.route("/services")
def mostraservices():
    return render_template("services.html")

app.run()