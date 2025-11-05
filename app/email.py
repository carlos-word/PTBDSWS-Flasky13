import requests
from datetime import datetime
from flask import current_app

def send_simple_message(to, subject, newUser):
    app = current_app

    print('Enviando mensagem (POST) - função send simple...', flush=True)
    print('variáveis')
    print('URL: ' + str(current_app.config.get('API_URL')), flush=True)
    print('api: ' + str(current_app.config.get('API_KEY')), flush=True)
    print('from: ' + str(current_app.config.get('API_FROM')), flush=True)
    print('to: ' + str(to), flush=True)
    print('subject: ' + str(current_app.config.get('FLASKY_MAIL_SUBJECT_PREFIX')) + ' ' + subject, flush=True)
    print('text: ' + "Novo usuário cadastrado: " + newUser, flush=True)

    resposta = requests.post(current_app.config.get('API_URL'),
                             auth=("api", current_app.config.get('API_KEY')), data={"from": current_app.config.get('API_FROM'),
                                                                        "to": to,
                                                                        "subject": current_app.config.get('FLASKY_MAIL_SUBJECT_PREFIX') + ' ' + subject,
                                                                        "text": "Novo usuário cadastrado no sistema do Cauê Weber PT3032205: " + newUser})

    print('Enviando mensagem (Resposta)...' + str(resposta) + ' - ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), flush=True)
    return resposta
