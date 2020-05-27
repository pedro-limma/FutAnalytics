from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha512 as crypto

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def gen_hash(self):
        self.password = crypto.hash(self.password)


    def verify_password(self, password):
        return crypto.verify(password, self.password)