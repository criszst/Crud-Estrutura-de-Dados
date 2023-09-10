from main import *
from script import validateCpf

app = Gui()
rows = 'Coloque os dados de forma valida.'

class VerifyData:
    def __init__(self,
                 name = app.txtNome.get(), second_name = app.txtSobrenome.get(),
                 email = app.txtEmail.get(), cpf = app.txtCpf.get()):
       self.name = name
       self.second_name = second_name
       self.email = email
       self.cpf = cpf

    def validate(self, name, second_name, email, cpf):
        if (NameAndSecond(name, second_name) and
            Email(email) and
            Cpf(cpf)):

            return True

        else:
            return False

    def response(self):
        app.listClientes.insert(END, rows)

def NameAndSecond(name, second_name):
    if str(name).replace('-', '').isdigit() or str(second_name).replace('-', '').isdigit():
        rows = f'Não é permitido nomes que possuem numeros'
        app.listClientes.insert(END, rows)
        return False

    return True

def Email(email):
    words_ok: list[str] = ['@gmail', "@"]

    for words in words_ok:
        if words.lower() not in email.lower():
            rows = 'Email nao aceito'
            app.listClientes.insert(END, rows)
            return False

    return True

def Cpf(cpf):
    print(validateCpf.validate(cpf))
    if not validateCpf.validate(cpf):
        rows = 'CPF invalido'
        app.listClientes.insert(END, rows)
        return False

    return True

