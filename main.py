from tkinter import *
import customtkinter as ct

class Gui:
    x_pad = 5
    y_pad = 5
    width_entry = 200
    btnWidth = 200

    window = ct.CTk()
    window.wm_title("CRUD SQL")
    window.geometry("960x582")
    window.grid_columnconfigure(2, weight=4)

    ct.set_appearance_mode("System")

    sidebar_frame = ct.CTkFrame(window, width=140, corner_radius=0)
    sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
    sidebar_frame.grid_rowconfigure(4, weight=1)

    txtNome = ct.StringVar()
    txtSobrenome = ct.StringVar()
    txtEmail = ct.StringVar()
    txtCpf = ct.StringVar()

    entNome = ct.CTkEntry(sidebar_frame, width=width_entry, placeholder_text = 'Nome')
    entSobrenome = ct.CTkEntry(sidebar_frame, width=width_entry, placeholder_text= 'Sobrenone')
    entEmail = ct.CTkEntry(sidebar_frame, width=width_entry, placeholder_text = 'Email')
    entCpf = ct.CTkEntry(sidebar_frame, width=width_entry, placeholder_text = 'CPF')


    listClientes = Listbox(window, width=120)
    scrollClientes = ct.CTkScrollbar(window)

    btnViewAll = ct.CTkButton(
        sidebar_frame, text="Ver Todos", corner_radius=20, width=btnWidth
    )

    btnBuscar = ct.CTkButton(
        sidebar_frame, text="Buscar", width=btnWidth, corner_radius=20,
    )

    btnInserir = ct.CTkButton(
        sidebar_frame, text="Inserir", width=btnWidth, corner_radius=20
    )

    btnUpdate = ct.CTkButton(
        sidebar_frame, text="Atualizar", width=btnWidth, corner_radius=20
    )

    btnDel = ct.CTkButton(
        sidebar_frame, text="Deletar", width=btnWidth, corner_radius=20
    )
    btnClose = ct.CTkButton(
        sidebar_frame, text="Fechar", width=btnWidth, corner_radius=20,
    )

    entNome.grid(row=0, column=0, padx=x_pad, pady=y_pad)
    entSobrenome.grid(row=1, column=0, padx=x_pad, pady=y_pad)
    entEmail.grid(row=2, column=0,padx=x_pad, pady=y_pad)
    entCpf.grid(row=3, column=0, padx=x_pad, pady=y_pad)

    listClientes.grid(row=0, column=2, rowspan=10)
    scrollClientes.grid(row=0, column=6, rowspan=10)

    btnViewAll.grid(row=4, column=0,  padx=x_pad, pady=y_pad)
    btnBuscar.grid(row=5, column=0, padx=x_pad, pady=y_pad)
    btnInserir.grid(row=6, column=0,  padx=x_pad, pady=y_pad)
    btnUpdate.grid(row=7, column=0,  padx=x_pad, pady=y_pad)
    btnDel.grid(row=8, column=0, padx=x_pad, pady=y_pad)
    btnClose.grid(row=9, column=0, padx=x_pad, pady=y_pad)

    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    for child in window.winfo_children():
        widget_class = child.__class__.__name__

        if widget_class == "Button":
            child.grid_configure(sticky="WE", padx=x_pad, pady=y_pad)

        elif widget_class == "ListBox":
            child.grid_configure(sticky="NS", padx=0, pady=0)

        elif widget_class == "ScrollBar":
            child.grid_configure(sticky="NS", padx=0, pady=0)

        else:
            child.grid_configure(sticky="N", padx=x_pad, pady=x_pad)

    @staticmethod
    def run():
        Gui.window.mainloop()
