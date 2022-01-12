from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# Cores
co0 = "#f0f3f5" #Preto
co1 = "#feffff" #Branco
co2 = "#3fb5a3" #Verde
co3 = "#38576b" #Valor
co4 = "#403d3d" #Letra

# Criando a janela
janela = Tk()
janela.title('Login')
janela.geometry('330x330')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

i_reembolso = PhotoImage(file='dinheiro.png')
janela.iconphoto(False, i_reembolso)

# Ícone Usuário
i_usuario_temp = Image.open('cadeado.png')
i_usuario_new = i_usuario_temp.resize((28,28))
i_usuario = ImageTk.PhotoImage(i_usuario_new)

# Ícone Cadeado
i_cadeado_temp = Image.open('usuario.png')
i_cadeado_new = i_cadeado_temp.resize((30,30))
i_cadeado = ImageTk.PhotoImage(i_cadeado_new)

# Linha Verde
i_linha_verde_temp = Image.open('linhaverde.png')
i_linha_verde_new = i_linha_verde_temp.resize((210,5))
i_linha_verde = ImageTk.PhotoImage(i_linha_verde_new)

# Ícone Reembolso
i_reembolso_temp = Image.open('reembolso.png')
i_reembolso_new = i_reembolso_temp.resize((90,90))
i_reembolso = ImageTk.PhotoImage(i_reembolso_new)

#janela.iconphoto(False, p1)

# Dividindo a janela
frame_cima = Frame(janela, width=330, height=130, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, padx=0, pady=1, sticky=NSEW)
frame_baixo = Frame(janela, width=330, height=200, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

# Configurando Frame Cima
l_icone_reembolso = Label(frame_cima, image=i_reembolso, anchor=W, bg=co1)
l_icone_reembolso.place(x=130,y=30)

credenciais = ['teste', '123456']


def verifica_senha():
    usuario= e_usuario.get()
    senha = e_senha.get()

    if usuario == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin!')
    elif credenciais[0] == usuario and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta ' + credenciais[0])

    else:
        messagebox.showwarning('Erro', 'Verifique o nome e a senha.')

def cancelar():

    janela.destroy()

# Configurando o Frame Baixo
l_icone_usuario = Label(frame_baixo, image=i_usuario, anchor=NW, bg=co1)
l_icone_usuario.place(x=45,y=20)

e_usuario = Entry(frame_baixo, width=22, justify='left', font=('Ivy,12'), borderwidth=0)
e_usuario.place(x=85, y=22)

l_linha_usuario = Label(frame_baixo, image=i_linha_verde, anchor=NW, border=0)
l_linha_usuario.place(x=85,y=45)

# Senha
l_icone_senha = Label(frame_baixo, image=i_cadeado, anchor=NW, bg=co1)
l_icone_senha.place(x=45,y=60)

e_senha = Entry(frame_baixo, show='*', width=22, justify='left', font=('Ivy,12'), borderwidth=0)
e_senha.place(x=85, y=63)

l_linha_senha = Label(frame_baixo, image=i_linha_verde, anchor=NW, border=0)
l_linha_senha.place(x=85,y=87)

# Botão Submeter Arquivo
b_submeter = Button(frame_baixo, command=verifica_senha, text='Entrar', width=17, height=2, font=('Ivy 10 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_submeter.place(x=15,y=140)

# Botão Canncelar
b_cancelar = Button(frame_baixo, command=cancelar, text='Cancelar', width=17, height=2, font=('Ivy 10 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_cancelar.place(x=169,y=140)

janela.mainloop()