from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask("_name_")
SECRET_KEY = "pudim"
app.config.from_object(__name__)

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

# USER MOCKS
USERNAME = "admin"
PASSWORD = "admin"

@app.route('/')
def exibir_entradas():
    return render_template("exibir_entradas.html", entradas=posts)

@app.route('/inserir', methods=['POST'])
def inserir_entradas():
    novo_post = {
        "titulo": request.form['titulo'],
        "texto": request.form['texto']
    }

    posts.append(novo_post)
    return redirect(url_for('exibir_entradas'))

@app.route('/login', methods=["GET", "POST"])
def login(): 
    erro = ""
    if request.method == "POST":
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logado'] = True
            flash("logado com êxito")
            return redirect (url_for('exibir_entradas'))
        erro = "Usuário ou senha inválidos"
        print(request.form['username'], request.form ['password'])
        return "dados recebidos"
    return render_template('login.html',  erro=erro)

@app.route('/logout')
def logout():
    session.pop('logado', None)
    flash("Logout efetuado com sucesso!")
    return redirect(url_for('exibir_entradas'))