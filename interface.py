"""#from tkinter import *
import tkinter as tk
from tkinter import *

class Gui():
    #Classe da Interface Grafica
    x_pad = 5
    y_pad = 3
    width_entry = 30
    
    #Criando janela    
    window = tk.Tk()
    window.wm_title("PYSQL versao 1.0")  
    
    # Definição das variáveis que recebem os dados inseridos pelo user
    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar() 
    
    lblnome = Label(window, text="Nome")
    lblsobrenome = Label(window, text="Sobrenome")
    lblemail = Label(window, text="Email")
    lblcpf = Label(window, text="CPF")
    
    entNome = Entry(window, textvariable = txtNome, width = width_entry)
    entSobrenome = Entry(window, textvariable = txtSobrenome, width = width_entry)
    entEmail = Entry(window, textvariable = txtEmail, width = width_entry)
    entCPF = Entry(window, textvariable = txtCPF, width = width_entry)
    
    listClientes = Listbox(window, width = 100)
    scrollClientes = Scrollbar(window)
    btnViewAll = Button(window, text="Ver todos")
    btnBuscar = Button(window, text="Buscar")
    btnInserir = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Update")
    btnDelete = Button(window, text="Deletar")
    btnClose = Button(window, text="Fechar")
    
    lblnome.grid(row=0, column=0)
    lblsobrenome.grid(row=1, column=0)
    lblemail.grid(row=2, column=0)
    lblcpf.grid(row=3, column=0)
    entNome.grid(row=0, column=1, padx=50, pady=50)
    entSobrenome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)
    listClientes.grid(row=0, column=2, rowspan=10)
    scrollClientes.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2) 
    btnDelete.grid(row=8, column=0, columnspan=2) 
    btnClose.grid(row=9, column=0, columnspan=2) 
    
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)
    
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='NS')
    
    def run(self):
        Gui.window.mainloop()"""
        
        
"""Nesta versão, a classe Gui é corrigida para encapsular todos os seus 
componentes e funcionalidades. O método setup_layout() organiza a disposição 
dos elementos na janela, e o método run() inicia a interface gráfica quando 
o arquivo é executado como um script principal."""        
import tkinter as tk
from tkinter import StringVar

class Gui:
    # Atributos de classe
    x_pad = 5
    y_pad = 3
    width_entry = 30
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.wm_title("PYSQL versao 1.0")  

        # Variáveis de controle para os campos de entrada
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar() 
        
        # Rótulos e campos de entrada
        self.lblnome = tk.Label(self.window, text="Nome")
        self.lblsobrenome = tk.Label(self.window, text="Sobrenome")
        self.lblemail = tk.Label(self.window, text="Email")
        self.lblcpf = tk.Label(self.window, text="CPF")
        
        self.entNome = tk.Entry(self.window, textvariable=self.txtNome, width=self.width_entry)
        self.entSobrenome = tk.Entry(self.window, textvariable=self.txtSobrenome, width=self.width_entry)
        self.entEmail = tk.Entry(self.window, textvariable=self.txtEmail, width=self.width_entry)
        self.entCPF = tk.Entry(self.window, textvariable=self.txtCPF, width=self.width_entry)
        
         # Lista de clientes, barra de rolagem e botões
        self.listClientes = tk.Listbox(self.window, width=100)
        self.scrollClientes = tk.Scrollbar(self.window)
        self.btnViewAll = tk.Button(self.window, text="Ver todos")
        self.btnBuscar = tk.Button(self.window, text="Buscar")
        self.btnInserir = tk.Button(self.window, text="Inserir")
        self.btnUpdate = tk.Button(self.window, text="Update")
        self.btnDelete = tk.Button(self.window, text="Deletar")
        self.btnClose = tk.Button(self.window, text="Fechar")
        
        self.setup_layout()

    def setup_layout(self):
        # Posicionamento dos elementos na interface usando grid
        self.lblnome.grid(row=0, column=0)
        self.lblsobrenome.grid(row=1, column=0)
        self.lblemail.grid(row=2, column=0)
        self.lblcpf.grid(row=3, column=0)
        self.entNome.grid(row=0, column=1, padx=50, pady=50)
        self.entSobrenome.grid(row=1, column=1)
        self.entEmail.grid(row=2, column=1)
        self.entCPF.grid(row=3, column=1)
        self.listClientes.grid(row=0, column=2, rowspan=10)
        self.scrollClientes.grid(row=0, column=6, rowspan=10)
        self.btnViewAll.grid(row=4, column=0, columnspan=2)
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnUpdate.grid(row=7, column=0, columnspan=2) 
        self.btnDelete.grid(row=8, column=0, columnspan=2) 
        self.btnClose.grid(row=9, column=0, columnspan=2) 
        
        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)
        
        for child in self.window.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky='WE', padx=self.x_pad, pady=self.y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            elif widget_class == "Scrollbar":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                child.grid_configure(padx=self.x_pad, pady=self.y_pad, sticky='NS')
    
    def run(self):
        # Inicia o loop principal da interface gráfica
        self.window.mainloop()

# Inicialização da interface gráfica
if __name__ == "__main__":
    app = Gui()
    app.run()
        
    
 

    