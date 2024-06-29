# Projeto: Interface Gráfica com PySimpleGUI

Este projeto é uma interface gráfica simples desenvolvida com a biblioteca PySimpleGUI em Python. A interface permite que o usuário insira um e-mail, senha e escolha pastas para anexos e planilhas. Ao clicar no botão "Salvar", as informações fornecidas são impressas no console.

## Funcionalidades

- Inserção de e-mail.
- Inserção de senha.
- Seleção de pasta para anexos.
- Seleção de pasta para planilhas.
- Botão "Salvar" que exibe as informações inseridas no console.

## Requisitos

- Python 3.x
- PySimpleGUI

## Instalação

1. **Clone o repositório**:

   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um ambiente virtual**:

   ```sh
   python -m venv venv
   ```

3. **Ative o ambiente virtual**:

   - No Windows (cmd.exe):

     ```sh
     venv\Scripts\activate.bat
     ```

   - No Windows (PowerShell):

     ```sh
     venv\Scripts\Activate.ps1
     ```

   - No Git Bash ou Linux/Mac:

     ```sh
     source venv/Scripts/activate
     ```

4. **Instale as dependências**:

   ```sh
   pip install PySimpleGUI
   ```

## Como usar

1. **Execute o script**:

   ```sh
   python seu_script.py
   ```

2. **Preencha os campos e selecione as pastas**:

   - Insira seu e-mail.
   - Insira sua senha.
   - Escolha a pasta de anexos.
   - Escolha a pasta de planilhas.

3. **Clique em "Salvar"**:

   - As informações inseridas serão exibidas no console.

## Código

```python
import PySimpleGUI as sg

sg.theme('reddit')

layout = [
    [sg.Text('E-mail'), sg.Input(key='email')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.FolderBrowse('Escolher Pasta de Anexos', target='input_anexos'), sg.Input(key='input_anexos')],
    [sg.FolderBrowse('Escolher Pasta de Planilhas', target='input_planilhas'), sg.Input(key='input_planilhas')],
    [sg.Button('Salvar')],
]

janela = sg.Window('Principal', layout=layout)

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

janela.close()
```

## Contribuição

Se você quiser contribuir com este projeto, por favor, faça um fork do repositório, crie um branch para suas alterações e envie um pull request.

1. Faça um fork do projeto.
2. Crie um branch para suas alterações (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas alterações (`git commit -am 'Adiciona nova funcionalidade'`).
4. Envie para o branch (`git push origin feature/nova-funcionalidade`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
