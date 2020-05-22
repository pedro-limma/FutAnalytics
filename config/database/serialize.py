from flask_marshmallow import Marshmallow
from config.database.model import Users
ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = Users

