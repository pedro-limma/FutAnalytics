from flask import Blueprint, make_response, request, url_for, redirect, render_template, current_app
from config.database.model import Users
from config.database.serialize import UserSchema

session_bp = Blueprint('Session', __name__,  template_folder='../templates')

@session_bp.route('/create_user', methods=['GET','POST'])
def create_user():
    if request.method == 'POST':
        us = UserSchema()
        user = us.load(request.json)
        current_app.db.session.add(user)
        current_app.db.session.commit()
        return us.jsonify(user), 201


@session_bp.route('/read_user', methods=['GET'])
def read_user():
    us = UserSchema(many=True)
    result = Users.query.all()
    return us.jsonify(result), 200


@session_bp.route('/update_user/<identify>', methods=['GET', 'POST'])
def update_user(identify):
    if request.method == 'POST':
        us = UserSchema()
        query = Users.query.filter(Users.id == identify)
        query.update(request.json)
        current_app.db.session.commit()
        user = us.load(request.json)
        return us.jsonify(user), 201


@session_bp.route('/delete_user/<identify>', methods=['GET'])
def delete_user(identify):
    us = UserSchema(many=True)
    Users.query.filter(Users.id == identify).delete()
    current_app.db.session.commit()
    result = Users.query.all()
    return us.jsonify(result), 200
