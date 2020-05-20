from flask import \
    Blueprint,\
    render_template,\
    request,\
    make_response,\
    redirect,\
    url_for

home_bp = Blueprint('Home', __name__, template_folder='../templates/home.html')

#decorator para declaração de rota da aplicação
@home_bp.route('/home')
def home():
    logado = request.cookies.get('logado')
    if logado:
        username = request.cookies.get('username')
        return render_template("home.html", username=username)
    else:
        return redirect(url_for("Session.login"))