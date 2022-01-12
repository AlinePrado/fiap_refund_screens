from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

# Cores
co0 = "#f0f3f5" #Preto
co1 = "#feffff" #Branco
co2 = "#3fb5a3" #Verde
co3 = "#38576b" #Valor
co4 = "#403d3d" #Letra

# Criando a janela
janela = Tk()
janela.title('Formulário de Reembolso')
janela.geometry('330x330')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

i_reembolso = PhotoImage(file='dinheiro.png')
janela.iconphoto(False, i_reembolso)

# Dividindo a janela
frame_cima = Frame(janela, width=330, height=60, bg=co1, relief='flat')
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


def cancelar():

    janela.destroy()

# Configurando Frame Cima
l_nome = Label(frame_cima, text='Olá ' + credenciais[0], anchor=NW, font=('Ivy 14'), bg=co1, fg=co2)
l_nome.place(x=8,y=5)

l_descricao = Label(frame_cima, text = 'Formulário de Reembolso:', width=40, height=2, anchor=NW, font=('Ivy 11'), bg=co1, fg=co4)
l_descricao.place(x=8,y=35)

# Label Estabelecimento
l_estabelecimento = Label(frame_baixo, text = 'Estabelecimento', width=15, anchor=NW, font=('Ivy 11'), bg=co1, fg=co4)
l_estabelecimento.place(x=43,y=10)

e_estabelecimento = Entry(frame_baixo, width=16, justify='left', font=('Ivy 12'), highlightthickness=1, relief='solid')
e_estabelecimento.place(x=165,y=10)

l_consumidor = Label(frame_baixo, text = 'Consumidor', width=10, anchor=NW, font=('Ivy 11'), bg=co1, fg=co4)
l_consumidor.place(x=70,y=45)

e_consumidor = Entry(frame_baixo, width=16, justify='left', font=('Ivy 12'), highlightthickness=1, relief='solid')
e_consumidor.place(x=165,y=45)

l_produtos_comprados = Label(frame_baixo, text = 'Produtos Comprados', anchor=NW, width=18, font=('Ivy 11'), bg=co1, fg=co4)
l_produtos_comprados.place(x=10,y=80)

e_produtos_comprados = Text(frame_baixo, width=16, height=4, font=('Ivy 12'), highlightthickness=1, relief='solid')
e_produtos_comprados.place(x=165,y=80)

l_valor_total = Label(frame_baixo, text = 'Valor Total', width=10, anchor=NW, font=('Ivy 11'), bg=co1, fg=co4)
l_valor_total.place(x=80,y=170)

e_valor_total = Entry(frame_baixo, width=16, justify='left', font=('Ivy 12'), highlightthickness=1, relief='solid')
e_valor_total.place(x=165,y=170)

# Botão Submeter Arquivo
b_submeter = Button(frame_baixo, text='Confirmar', width=17, height=2, font=('Ivy 10 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_submeter.place(x=15,y=210)

# Botão Canncelar
b_cancelar = Button(frame_baixo, command=cancelar, text='Cancelar', width=17, height=2, font=('Ivy 10 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_cancelar.place(x=169,y=210)

janela.mainloop()