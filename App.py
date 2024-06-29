import PySimpleGUI as sg

sg.theme('reddit')

layout = [
    [sg.Text('E-mail'), sg.Input(key='email')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.FolderBrowse('Escolher Pasta de Anexos', target='input_anexos'),sg.Input(key='input_anexos')],
    [sg.FolderBrowse('Escolher Pasta de Planilhas', target='input_planilhas'),sg.Input(key='input_planilhas')],
    [sg.Button('Salvar')],
]

janela = sg.Window('Principal', layout = layout)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar':
        email = values['email']
        senha = values['senha']
        anexos = values['input_anexos']
        planilha = values['input_planilhas']

        print(f'O e-mail digitado foi {email}')
        print(f'A senha digitada foi {senha}')
        print(f'O caminho do anexo digitado foi {anexos}')
        print(f'O caminho da planilha digitado foi {planilha}')