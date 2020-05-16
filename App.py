from flask import Flask, render_template #importando o módulo

app = Flask(__name__)
#criando o objeto

#decorator para declaração de rota da aplicação


@app.route("/<user>", methods=["GET"])
def helloWorld(user):
    return render_template("home.html", nomes=user)


@app.route("/cardapio", methods=["GET"])
def helloPeople():
    cardapio = {
        "frutas": [
            "maçã",
            "pêra",
            "Banana"
        ],
        "Principal": [
            "carne",
            "Peixe",
            "Camarão empanado"
        ]
    }
    return cardapio

#rodando o app com o debug  ativado na porta 3333
app.run(debug=True, port=3333)
