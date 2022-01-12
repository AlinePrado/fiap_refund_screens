from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

# Cores
co0 = "#f0f3f5" #Preto
co1 = "#feffff" #Branco
co2 = "#3fb5a3" #Verde
co3 = "#38576b" #Valor
co4 = "#403d3d" #Letra

# Criando a janela
janela = Tk()
janela.title('Reembolso de Nota Fiscal')
janela.geometry('330x330')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

i_reembolso = PhotoImage(file='dinheiro.png')
janela.iconphoto(False, i_reembolso)

# Dividindo a janela
frame_cima = Frame(janela, width=330, height=80, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, padx=0, pady=1, sticky=NSEW)

frame_baixo = Frame(janela, width=330, height=300, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

credenciais = ['teste', '123456']

categorias = [
    'Alimentação',
    'Gasolina',
    'Internet',
    'Viagem'
]

# Método para Selecionar Imagem
def selecionarImagem():
    filetypes = (
        ('JPEG Files', '*.jpg'),
        ('PNG Files', '*.png')
    )

    filename = askopenfilename(filetypes=filetypes)
    e_diretorio.delete(0, END)
    e_diretorio.insert(0, filename)

def submeter_documento():

    diretorio = e_diretorio.get()

    if (diretorio) != '':
        messagebox.showinfo('Confirmação','Arquivo submetido com sucesso!')
    else:
        messagebox.showwarning('Erro', 'Nenhum arquivo foi selecionado.')

def cancelar():

    janela.destroy()

# Configurando Frame Cima
l_nome = Label(frame_cima, text='Olá ' + credenciais[0], anchor=NW, font=('Ivy 14'), bg=co1, fg=co2)
l_nome.place(x=8,y=5)

l_descricao = Label(frame_cima, text = 'Selecione as informações abaixo para solicitar \n o reembolso:', width=40, height=2, anchor=NW, font=('Ivy 11'), bg=co1, fg=co4)
l_descricao.place(x=8,y=35)

# Label Categoria
l_categorias = Label(frame_baixo, text = 'Selecione uma Categoria', width=18, anchor=NW, font=('Ivy 11'), bg=co1, fg=co4)
l_categorias.place(x=10,y=25)

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set(categorias[0])

# Create Dropdown menu
drop = OptionMenu(frame_baixo, clicked, *categorias)
drop.config(width=33, anchor=NW, font='Ivy 10')
drop.pack()
drop.place(x=10,y=50)

# Label Selecionar Arquivo
l_arquivo = Label(frame_baixo, text = 'Selecione um Arquivo', width=18, anchor=NW, font=('Ivy 11'), bg=co1, fg=co4)
l_arquivo.place(x=10,y=90)

# Diretório
e_diretorio = Entry(frame_baixo, width=30, justify='left', font=('Ivy 12'), highlightthickness=1, relief='solid')
e_diretorio.place(x=10,y=112)

# Selecionar Arquivo
b_selecionar_arquivo = Button(frame_baixo, command=selecionarImagem, text='...', width=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_selecionar_arquivo.place(x=290,y=111)

# Botão Submeter Arquivo
b_submeter = Button(frame_baixo, command=submeter_documento, text='Submeter', width=17, height=2, font=('Ivy 10 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_submeter.place(x=15,y=190)

# Botão Canncelar
b_cancelar = Button(frame_baixo, command=cancelar, text='Cancelar', width=17, height=2, font=('Ivy 10 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_cancelar.place(x=169,y=190)

janela.mainloop()