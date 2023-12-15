import os
import smtplib
from email.message import EmailMessage
import PySimpleGUI as sg

def enviar_email(email_address, email_password, to_address, assunto, conteudo):
    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = email_address
    msg['To'] = to_address
    msg.set_content(conteudo)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

def main():
    sg.theme('DarkRed1')
    
    layout = [
        [sg.Text('Endereço de Email:'), sg.Input(key='-EMAIL-', size=(30, 1))],
        [sg.Text('Senha:'), sg.Input(key='-PASSWORD-', password_char='*', size=(30, 1))],
        [sg.Text('Destinatário:'), sg.Input(key='-TO-', size=(30, 1))],
        [sg.Text('Assunto:'), sg.Input(key='-SUBJECT-', size=(30, 1))],
        [sg.Text('Conteúdo:'), sg.Input(key='-CONTENT-', size=(30, 1))],
        [sg.Button('Enviar Email'), sg.Button('Sair')]
    ]

    window = sg.Window('Automação de Email', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Sair':
            break
        elif event == 'Enviar Email':
            email_address = values['-EMAIL-']
            email_password = values['-PASSWORD-']
            to_address = values['-TO-']
            assunto = values['-SUBJECT-']
            conteudo = values['-CONTENT-']

            try:
                enviar_email(email_address, email_password, to_address, assunto, conteudo)
                sg.popup('Email enviado com sucesso!')
            except Exception as e:
                sg.popup_error(f'Erro ao enviar o email:\n{str(e)}')

    window.close()

if __name__ == '__main__':
    main()
