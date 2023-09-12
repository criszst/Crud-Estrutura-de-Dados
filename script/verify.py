from main import *
from script import validateCpf

import backend as core

interface = Gui()


class VerifyData:
    def __init__(
        self,
        name=interface.entNome.get(),
        second_name=interface.entSobrenome.get(),
        email=interface.entEmail.get(),
        cpf=interface.entCpf.get(),
    ):
        self.name = name
        self.second_name = second_name
        self.email = email
        self.cpf = cpf

    def validate(self, name, second_name, email, cpf):
        if (
            NameAndSecond(name, second_name)
            and Email(email)
            and Cpf(cpf)
            and verifyUserExist(email, cpf)
        ):
            return True
        else:
            return False


def verifyUserExist(email, cpf):
    all_clients = core.view()

    for cl in all_clients:
        if email in cl[3] or cpf in cl[4]:
            interface.listClientes.insert(END, "Esse usuario ja existe")
            return False

    return True


def NameAndSecond(name, second_name):
    name_str = str(name)
    second_str = str(second_name)

    if (
        name_str.replace("-", "").isdigit()
        or second_str.replace("-", "").isdigit()
        or name_str == ""
        or second_str == ""
    ):
        print(name_str)
        interface.listClientes.insert(END, 'Escreva um nome valido')
        return False

    return True


def Email(email):
    words_ok: list[str] = ["@gmail.com", "@gmail"]

    for words in words_ok:
        if words.lower() not in email.lower():
            interface.listClientes.insert(END, "Email invalido")
            return False

    return True


def Cpf(cpf):
    if not validateCpf.validate(cpf):
        interface.listClientes.insert(END, "CPF invalido")
        return False

    return True
