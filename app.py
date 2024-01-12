from interface import *     # Importa a classe da interface gráfica
import backend as core      # Importa as operações do banco de dados
from tkinter import END     # Importa a constante END do módulo tkinter

app = None
selected = None     # Variável para armazenar o item selecionado na lista

# Funções para manipulação dos dados e atualização da interface
def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)
        
def search_command():
    app.listClientes.delete(0, END)
    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END, r)

def insert_comand():
    core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()
    
def update_command():
    core.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()
    
def delete_command():
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
    app.entEmail.delete(0, END)
    app.entEmail.insert(END, selected[3])
    app.entCPF.delete(0, END)
    app.entCPF.insert(END, selected[4])
    return selected

if __name__=="__main__":
   app = Gui()
   app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)
   
    # Configuração dos comandos dos botões na interface
   app.btnViewAll.configure(command=view_command)
   app.btnBuscar.configure(command=search_command)
   app.btnInserir.configure(command=insert_comand)
   app.btnUpdate.configure(command=update_command)
   app.btnDelete.configure(command=delete_command)
   app.btnClose.configure(command=app.window.destroy)
   app.run()