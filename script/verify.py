from main import *
from script import validateCpf

import backend as core

interface = Gui()
rows = 'Insira dados válidos.'

class VerifyData:
    def __init__(self, name = interface.txtNome.get(), second_name = interface.txtSobrenome.get(),
                       email = interface.txtEmail.get(), cpf = interface.txtCpf.get()):
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
        interface.listClientes.insert(END, rows)

def verifyUserExist(email, cpf):

    allClients = core.view()

    for cl in allClients:
        print(cl[3])
        print(cl[4])
        if email in cl[3] or cpf in cl[4]:

            return False

    return True


def NameAndSecond(name, second_name):
    if (str(name).replace('-', '').isdigit() or
        str(second_name).replace('-', '').isdigit() or
        str(name) == '' or str(second_name) == ''):

        rows = f'Escreva um nome valido'
        interface.listClientes.insert(END, rows)
        return False

    return True

def Email(email):
    words_ok: list[str] = ['@gmail', '@']

    for words in words_ok:
        if words.lower() not in email.lower():
            rows = 'Email nao aceito'
            interface.listClientes.insert(END, rows)
            return False

    return True

def Cpf(cpf):
    if not validateCpf.validate(cpf):
        rows = 'CPF invalido'
        interface.listClientes.insert(END, rows)
        return False

    return True