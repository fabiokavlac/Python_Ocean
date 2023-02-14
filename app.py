from flask import Flask, render_template

app = Flask("_name_")

#POSTS MOCK

posts = [
    {
        "titulo":"Post1",
        "texto":"Olha eu"
    },
    {
        "titulo":"Post2",
        "texto":"Olha eu de novo"
    }
]

@app.route('/')
def exibir_entradas():
    return render_template("exibir_entradas.html")

@app.route('/pudim')
def pudim():
    return "<h1>Eu gosto de pudim</h1>"

