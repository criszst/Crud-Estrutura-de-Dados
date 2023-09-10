from main import *
import backend as core

app = None

wordsOk: list[str] = ['@gmail', "@"]

## Default ignored files
#/shelf/
#/workspace.xml
# Editor-based HTTP Client requests
#/httpRequests/
# Datasource local storage ignored files
#/dataSources/
#/dataSources.local.xml

def verifyData():
    for words in app.txtEmail.get():
        if words.lower() not in app.txtEmail.get().lower():
            rows = 'email nao aceito'
            app.listClientes.insert(END, rows)
            return False

    return True

#teste
def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)

def search_command():
    app.listClientes. delete(0, END)

    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(),app.txtCpf.get())
    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
    if verifyData:
        core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCpf.get())
        view_command()

def update_command():
    core.update(selected[0], app.txtNome.get(),app.txtSobrenome.get(),app.txtEmail.get (), app.txtCpf.get())
    view_command()

def del_command():
    id = selected[0]
    core.delete(id)
    view_command()

def getSelectedRow(event):
    global selected
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)

    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])

    app.entSobrenome.delete(0, END)
    app.entSobrenome.insert(END, selected[2])

    app.entEmail.delete (0, END)
    app.entEmail.insert(END, selected[3])

    app.entCpf.delete(0, END)
    app.entCpf.insert(END, selected[4])
    return selected

if __name__ == "__main__":
    app = Gui()
    app.listClientes.bind('<<ListboxSelect>> ', getSelectedRow)

app.btnViewAll.configure(command=view_command)
app.btnBuscar.configure(command=search_command)
app.btnInserir.configure(command=insert_command)
app.btnUpdate.configure(command=update_command)
app.btnDel.configure(command=del_command)
app.btnClose.configure(command=app.window.destroy)
app.run()