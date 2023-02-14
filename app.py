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
    },
    {
        "titulo":"Post3",
        "texto":"Olha eu de novo de novo"
    }
]

@app.route('/')
def exibir_entradas():
    return render_template("exibir_entradas.html", entradas=posts)
