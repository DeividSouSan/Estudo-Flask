#26:38
from flask import Flask, render_template

app = Flask(__name__)

# PRIMEIRA PARGINA DO SITE

# Entendendo o conceito de ROUTE: e basicamente definir o link para uma pagina.
@app.route("/")
# Entendendo o conceito de FUNCAO: e o que vai ser exibido na pagina.
def homepage():
    return render_template('homepage.html')

@app.route('/contatos')
def usuarios():
    return 'Pagina mostrando os contatos'

# Pagina com "rota" dinamica
@app.route("/usuario/<nome_usuario>")
def usuario(nome_usuario):
    return render_template('usuario.html', nome_usuario=nome_usuario) 

# COLOCANDO O SITE NO AR
if __name__ == '__main__':
    app.run(debug=True) # debug=True F5 atualiza o site sem necessidade de re-executar o arquivo