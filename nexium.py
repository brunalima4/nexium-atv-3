import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  

janela= tk.Tk()
janela.geometry("1250x800")
janela.configure(bg= "#cbe4d4")

usuario_cadastrado= ""
senha_cadastrada= ""

def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()

def logar():
    global usuario_cadastrado
    global senha_cadastrada

    if usuariol.get() == usuario_cadastrado and senhal.get() == senha_cadastrada:
        limpar_tela()
        frame = tk.Frame(janela)
        frame.pack(padx=10, pady=10)

        imagem = Image.open(r"u:\Bruna\interfacenexium.png")
        imagem = imagem.resize((1200, 700))
        imagem_tk = ImageTk.PhotoImage(imagem)
        label_img = tk.Label(frame, image=imagem_tk)
        label_img.image = imagem_tk
        label_img.pack(pady=10)

        label_boas_vindas = tk.Label(frame, text="Bem-vindo à Tela Principal!", font=("Arial", 16))
        label_boas_vindas.pack(pady=10)
   
    else:
        messagebox.showerror("Erro de Login", "Usuário ou senha incorretos!")

def limpar():
    global usuario_cadastrado, senha_cadastrada
    usuario_cadastrado = usuario.get()
    senha_cadastrada = senha.get()
    senha.delete(0, tk.END)
    usuario.delete(0, tk.END)

#Cadastro
cad= tk.Label(janela,font=("Californian FB", 35), text= "Cadastro", bg= "#cbe4d4" )
cad.pack(pady= 10, anchor="w", padx= 30)

#Usuário
juntos = tk.Frame(janela, bg= "#cbe4d4")
juntos.pack(pady=5, anchor= "w")

usu= tk.Label(juntos,font=("Californian FB", 15), text="Usuário:", bg= "#cbe4d4")
usu.pack(pady= 10, side= "left")

usuario= tk.Entry(juntos, font=("Californian FB", 15))
usuario.pack(pady= 10, side= "left")

#Senha
juntos2 = tk.Frame(janela, bg= "#cbe4d4")
juntos2.pack(pady=5, anchor= "w")

sen= tk.Label(juntos2, font=("Californian FB", 15), text="Senha:", bg= "#cbe4d4")
sen.pack(pady= 10, side= "left")

senha= tk.Entry(juntos2, font=("Californian FB", 15), show= "*")
senha.pack(pady= 10, side= "left")

#CONFIRMAR
conf= tk.Button(janela, text= "Corfirmar", font=("Californian FB", 15), width= 10, command= limpar)
conf.pack(pady= 10, anchor= "w", padx= "100")

#Ou
ou= tk.Label(janela, text= "-------- Ou ---------", bg= "#cbe4d4", font=("Californian FB", 30))
ou.pack(pady= 10, anchor= "w", padx= 30)

#login

log= tk.Label(janela,font=("Californian FB", 25), text= "Login", bg= "#cbe4d4" )
log.pack(pady= 10, anchor="w", padx= 30)

#Usuário do Login
juntos3 = tk.Frame(janela, bg= "#cbe4d4")
juntos3.pack(pady=5, anchor= "w")

usua= tk.Label(juntos3,font=("Californian FB", 15), text="Usuário:", bg= "#cbe4d4")
usua.pack(pady= 10, side= "left")

usuariol= tk.Entry(juntos3, font=("Californian FB", 15))
usuariol.pack(pady= 10, side= "left")

#Senha do Login
juntos4 = tk.Frame(janela, bg= "#cbe4d4")
juntos4.pack(pady=5, anchor= "w")

senl= tk.Label(juntos4, font=("Californian FB", 15), text="Senha:", bg= "#cbe4d4")
senl.pack(pady= 10, side= "left")

senhal= tk.Entry(juntos4, font=("Californian FB", 15), show="*")
senhal.pack(pady= 10, side= "left")

#Entrar
ent= tk.Button(janela, text= "Entrar", font=("Californian FB", 15), width= 10, command= logar)
ent.pack(pady= 10, anchor= "w", padx= "100")


janela.mainloop()
