from flask import render_template, session, redirect, url_for, current_app
from . import main  # blueprint
from .forms import NameForm
from app import db 
from app.models import User
from app.email import send_simple_message


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # Verifica se o usuário já existe
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            # Cria novo usuário
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False

            print('Verificando variáveis de ambiente: Server log do PythonAnyWhere', flush=True)
            print('FLASKY_ADMIN: ' + str(current_app.config.get('FLASKY_ADMIN')), flush=True)

            # Envia email se o admin estiver configurado
            if current_app.config.get('FLASKY_ADMIN'):
                print('Enviando mensagem...', flush=True)
                send_simple_message(
                    [current_app.config['FLASKY_ADMIN'], "flaskaulasweb@zohomail.com"],
                    'Novo usuário',
                    form.name.data
                )
                print('Mensagem enviada...', flush=True)
        else:
            session['known'] = True

        session['name'] = form.name.data
        return redirect(url_for('main.index'))

    users_list = User.query.order_by(User.username).all()

    return render_template(
        'index.html',
        form=form,
        name=session.get('name'),
        known=session.get('known', False),
        users=users_list
    )
