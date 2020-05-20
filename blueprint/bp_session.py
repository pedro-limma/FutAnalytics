from flask import Blueprint, make_response, request, url_for, redirect, render_template

session_bp = Blueprint('Session', __name__,  template_folder='../templates')

@session_bp.route('/login')
def login():
    return render_template("session.html")


@session_bp.route('/login_validation', methods=['POST'])
def login_validation():
    response = request.form.to_dict()
    username = response['username']
    response =  make_response(redirect(url_for("Home.home")))
    response.set_cookie("logado", "sS")
    response.set_cookie("username", username)
    return response