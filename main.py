from tkinter import *

class Gui:
    x_pad = 5
    y_pad = 3
    width_entry = 30

    window = Tk()
    window.wm_title('PYSQL versao 1.0')

    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCpf = StringVar()

    lblNome = Label(window, text="Nome")
    lblSobrenome = Label(window, text="Sobrenome")
    lblEmail = Label(window, text="Email")
    lblCpf = Label(window, text="CPF")

    entNome = Entry(window, textvariable=txtNome, width=width_entry)
    entSobrenome = Entry(window, textvariable=txtSobrenome, width=width_entry)
    entEmail = Entry(window, textvariable=txtEmail, width=width_entry)
    entCpf = Entry(window, textvariable=txtCpf, width=width_entry)

    listClientes = Listbox(window, width=100)
    scrollClientes = Scrollbar(window)

    btnViewAll = Button(window, text = 'Ver Todos')
    btnBuscar = Button(window, text = 'Buscar')
    btnInserir = Button(window, text = 'Inserir')
    btnUpdate = Button(window, text = 'Atualizar Selecionados')
    btnDel = Button(window, text = 'Deletar Selecionados')
    btnClose = Button(window, text = 'Fechar')

    lblNome.grid(row = 0, column = 0)
    lblSobrenome.grid(row = 1, column = 0)
    lblEmail.grid(row = 2, column = 0)
    lblCpf.grid(row = 3, column = 0)

    entNome.grid(row = 0, column = 1, padx = 50, pady = 50)
    entSobrenome.grid(row = 1, column = 1)
    entEmail.grid(row = 2, column = 1)
    entCpf.grid(row = 3, column = 1)

    listClientes.grid(row = 0, column = 2, rowspan = 10)
    scrollClientes.grid(row = 0, column= 6, rowspan = 10)

    btnViewAll.grid(row =4, column = 0, columnspan = 2)
    btnBuscar.grid(row = 5, column = 0, columnspan = 2)
    btnInserir.grid(row = 6, column = 0, columnspan = 2)
    btnUpdate.grid(row = 7, column = 0, columnspan = 2)
    btnDel.grid(row = 8, column = 0, columnspan = 2)
    btnClose.grid(row = 9, column = 0, columnspan = 2)

    listClientes.configure(yscrollcommand = scrollClientes.set)
    scrollClientes.configure(command = listClientes.yview)

    for child in window.winfo_children():
        widget_class = child.__class__.__name__

        if widget_class == 'Button':
            child.grid_configure(sticky = 'WE', padx = x_pad, pady = y_pad)

        elif widget_class == 'ListBox':
            child.grid_configure(sticky = 'NS', padx = 0, pady = 0)

        elif widget_class == 'ScrollBar':
            child.grid_configure(sticky = 'NS', padx = 0, pady = 0)

        else:
            child.grid_configure(sticky='N', padx=x_pad, pady=y_pad)

    def run(self):
        Gui.window.mainloop()