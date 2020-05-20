from flask import Flask, render_template #importando o módulo
from blueprint.bp_home import home_bp
from blueprint.bp_session import session_bp

app = Flask(__name__)
#criando o objeto
app.register_blueprint(home_bp)
app.register_blueprint(session_bp)

#rodando o app com o debug  ativado na porta 3333
app.run(debug=True, port=3333)
