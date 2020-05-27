#importando o módulo
from flask import Flask
from config.database.enviroment_variable import get_env_variable
from flask_migrate import Migrate
from blueprint.bp_home import home_bp
from blueprint.bp_user import session_bp
from flask_jwt_extended import JWTManager

from config.database.model import configure as db_config
from config.database.serialize import configure as ma_config

#criando o objeto
app = Flask(__name__)

#config banco de dados
POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")

DB_URL = 'postgresql+psycopg2://{user}:{passw}@{port}/{db}'.format(user=POSTGRES_USER, passw=POSTGRES_PW, port=POSTGRES_URL, db=POSTGRES_DB)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #silence the deprecation warning
app.config['JWT_SECRET_KEY'] = "pastelzinho de mel"
app.config['JWT_TOKEN_LOCATION'] = "cookies"
app.config['JWT_COOKIE_CSRF_PROTECT'] = False

db_config(app)
ma_config(app)
Migrate(app, app.db)


jwt = JWTManager(app)



app.register_blueprint(home_bp)
app.register_blueprint(session_bp)

#rodando o app com o debug  ativado na porta 3333
if __name__ == "__main__":
    app.run(debug=True, port=3333)
