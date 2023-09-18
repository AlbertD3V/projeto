from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/trampos")
def trampos():
    return render_template("trampos.html")

@app.route("/trampos/vagas")
def vagas():
    return render_template("vagas.html")

@app.route("/trampos/cursos")
def cursos():
    return render_template("cursos.html")

@app.route("/trampos/candidato")
def canditado():
    return render_template("candidato.html")


app.run(debug=True)