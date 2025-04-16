from interface import *     # Importa a classe da interface gráfica
import backend as core      # Importa as operações do banco de dados
from tkinter import END, messagebox    # Importa a constante END do módulo tkinter

app = None
selected = None     # Variável para armazenar o item selecionado na lista

def clean_input_command():
    app.txtNome.set("")
    app.txtSobrenome.set("")
    app.txtEmail.set("")
    app.txtCPF.set("")
    
# Funções para manipulação dos dados e atualização da interface
def view_command():
    try:
        rows = core.view()
        app.listClientes.delete(0, END)
        for r in rows:
            app.listClientes.insert(END, r)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar clientes: {str(e)}")
        
def search_command():
    try:
        rows = core.search(
            app.txtNome.get(), 
            app.txtSobrenome.get(), 
            app.txtEmail.get(), 
            app.txtCPF.get()
        )
        app.listClientes.delete(0, END)
        for r in rows:
            app.listClientes.insert(END, r)
        clean_input_command()  # Limpa os campos após a busca
    except Exception as e:
        messagebox.showerror("Erro", f"Erro na busca: {str(e)}")

def insert_command():
    try:
        core.insert(
            app.txtNome.get(), 
            app.txtSobrenome.get(), 
            app.txtEmail.get(), 
            app.txtCPF.get()
        )
        view_command()
        messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")
        clean_input_command()  # Limpa os campos após inserção
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def update_command():
    if not selected:
        messagebox.showwarning("Aviso", "Nenhum cliente selecionado")
        return
        
    try:
        core.update(
            selected[0], 
            app.txtNome.get(), 
            app.txtSobrenome.get(), 
            app.txtEmail.get(), 
            app.txtCPF.get()
        )
        view_command()
        messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
        clean_input_command()  # Limpa os campos após atualização
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def delete_command():
    if not selected:
        messagebox.showwarning("Aviso", "Nenhum cliente selecionado")
        return
        
    if not messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir este cliente?"):
        return
        
    try:
        core.delete(selected[0])
        view_command()
        messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")
        clean_input_command()  # Limpa os campos após deleção
    except Exception as e:
        messagebox.showerror("Erro", str(e))
    
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
   app.btnInserir.configure(command=insert_command)
   app.btnUpdate.configure(command=update_command)
   app.btnDelete.configure(command=delete_command)
   app.btnClose.configure(command=app.window.destroy)
   app.run()