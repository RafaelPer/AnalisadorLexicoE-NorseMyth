from tkinter import *
from tkinter import filedialog
import os
from lexer import *

janela = Tk()  # Definindo tela principal

janela.title("Compilador e-NorseMyth")  # Definindo titulo da janela principal


# |Funções|

# __|Fechar Janela|
def CloseWindow():
    janela.destroy()

# __|Importar Arquivo|
def importArq():
    global arq
    global file_path
    filename = filedialog.askopenfilename(initialdir="/", title="Selecione Um Arquivo", filetypes=(("Arquivos e-NorseMyth", "*.ensm"), ("all files", "*.*")))
    file_path = filename
    nameArquivo = os.path.basename(filename)
    print(filename)
    print(nameArquivo)
    if filename != None:
        if nameArquivo.endswith('.ensm'):
            #print("tem extensão .ensm")
            if filename != "":
                txt_I.configure(state=NORMAL)
                txt_I.delete('1.0', END)
                txt_I.insert(INSERT, filename)
                txt_I.configure(state=DISABLED)

                #da = open(filename, encoding="utf8")
                #print(da.read())

                txt_CF.configure(state=NORMAL)
                txt_CF.delete('1.0', END)
                with open(filename, encoding="utf8") as data:
                    d = data.read()
                    #d.replace(" -- ", "d")
                    # txt_CF.insert(INSERT, line)
                arq = d
                txt_CF.insert(INSERT, d)
                txt_CF.configure(state=DISABLED)

                txt_C.configure(state=NORMAL)
                txt_C.delete('1.0', END)
                txt_C.insert(INSERT, "Erros e analises")
                txt_C.configure(state=DISABLED)

                bt_AL.configure(state=NORMAL)
                bt_AS.configure(state=DISABLED)
            else:
                txt_I.configure(state=NORMAL)
                txt_I.delete('1.0', END)
                txt_I.insert(INSERT, "Por Favor Importe Um Arquivo")
                txt_I.configure(state=DISABLED)

                txt_CF.configure(state=NORMAL)
                txt_CF.delete('1.0', END)
                txt_CF.insert(INSERT, "Codigo Fonte")
                txt_CF.configure(state=DISABLED)

                txt_C.configure(state=NORMAL)
                txt_C.delete('1.0', END)
                txt_C.insert(INSERT, "Erros e analises")
                txt_C.configure(state=DISABLED)

                bt_AS.configure(state=DISABLED)
                bt_AL.configure(state=DISABLED)
        else:
            txt_I.configure(state=NORMAL)
            txt_I.delete('1.0', END)
            txt_I.insert(INSERT, "ARQUIVO INVALIDO")
            txt_I.configure(state=DISABLED)

            txt_CF.configure(state=NORMAL)
            txt_CF.delete('1.0', END)
            txt_CF.insert(INSERT, "Codigo Fonte")
            txt_CF.configure(state=DISABLED)

            txt_C.configure(state=NORMAL)
            txt_C.delete('1.0', END)
            txt_C.insert(INSERT, "Erros e analises")
            txt_C.configure(state=DISABLED)

            bt_AS.configure(state=DISABLED)
            bt_AL.configure(state=DISABLED)
        #print
        #"I got %d bytes from this file." % len(data)
    else:
        txt_I.configure(state=NORMAL)
        txt_I.delete('1.0', END)
        txt_I.insert(INSERT, "Por Favor Importe Um Arquivo")
        txt_I.configure(state=DISABLED)

        txt_CF.configure(state=NORMAL)
        txt_CF.delete('1.0', END)
        txt_CF.insert(INSERT, "Codigo Fonte")
        txt_CF.configure(state=DISABLED)

        txt_C.configure(state=NORMAL)
        txt_C.delete('1.0', END)
        txt_C.insert(INSERT, "Erros e analises")
        txt_C.configure(state=DISABLED)

        bt_AS.configure(state=DISABLED)
        bt_AL.configure(state=DISABLED)

# analisador lexico
def AnalisarLexicamente():
    console, error = realizarAnaliseLexica(arq)
    print(console)
    print(error)
    if error == "not error":
        bt_AS.configure(state=NORMAL)
    else:
        bt_AS.configure(state=DISABLED)
    txt_C.configure(state=NORMAL)
    txt_C.delete('1.0', END)
    for c in console:
        txt_C.insert(INSERT, c+"\n----------------\n")
    txt_C.configure(state=DISABLED)



# |Fim Funções|


# |Definições de Instancias|



# __|Caixa de Texto Que Vai Ter o Nome Do Arquivo De Codigo-Fonte|

#txt_I = Text(janela, yscrollcommand=scb1.set, width="64", height="1")
txt_I = Text(janela, width="64", height="1")

# __|Caixa de Texto Console|
txt_C = Text(janela, width="45", height="30")

# __|Caixa de Texto Codigo-Fonte|
txt_CF = Text(janela, width="45", height="28")

# __|Titulo Codigo Fonte|
lb_CF = Label(janela, text="Codigo Fonte e-NorseMyth", fg="#60412b", bg="#dde2e3", width="54")

# __|Titulo Console|
lb_C = Label(janela, text="Console", fg="#60412b", bg="#dde2e3", width="54")

# __|Botão Analisador Lexico|
bt_AL = Button(janela, width="35", text="Analisar Lexicamente", fg="#60412b", bg="#dde2e3", command=AnalisarLexicamente, state=DISABLED)

# __|Botão Analisador Sintatico|
bt_AS = Button(janela, width="35", text="Analisar Sintaticamente", fg="#60412b", bg="#dde2e3", state=DISABLED)

# __|Botão Importar Arquivo|
bt_I = Button(janela, width="35", text="Importar Arquivo", command=importArq, fg="#60412b", bg="#dde2e3")

# __|Botão Sair|
bt_S = Button(janela, width="110", text="Sair", command=CloseWindow, bg="red", fg="white")

# __|ScrollBar Codigo Fonte|
scb1 = Scrollbar(janela)

# __|ScrollBar Console|
scb2 = Scrollbar(janela)

# __|ScrollBar Codigo Fonte Horizontal|
scb3 = Scrollbar(janela, orient='horizontal')

# |Fim Definições de Instancias|


# |Configurando Instancias|

txt_I.place(x=268, y=593)  # Definindo localização na tela pelo metodo place do Tkinter
txt_I.insert(INSERT, "Por Favor Importe Um Arquivo")  # Inserindo texto na Text Box txt_I
txt_I.insert(END, "")
txt_I.bind("<1>", lambda event: txt_I.focus_set())  # fazendo o txt_I ser o foco
txt_I.configure(state=DISABLED)  # configurando o status do txt_I

txt_CF.place(x=5, y=30)  # Definindo localização na tela pelo metodo place do Tkinter
txt_CF.insert(INSERT, "Codigo Fonte")  # Inserindo texto na Text Box txt_CF
txt_CF.insert(END, "")
txt_CF.bind("<1>", lambda event: txt_CF.focus_set())  # fazendo o txt_CF ser o foco
txt_CF.configure(state=DISABLED, yscrollcommand=scb1.set, xscrollcommand=scb3.set)  # configurando o status do txt_CF e a parte de vinculação da scrollbar
txt_CF.config(wrap='none')

txt_C.place(x=400, y=30)  # Definindo localização na tela pelo metodo place do Tkinter
txt_C.insert(INSERT, "Erros e analises")  # Inserindo texto na Text Box txt_C
txt_C.insert(END, "")
txt_C.bind("<1>", lambda event: txt_C.focus_set())  # fazendo o txt_C ser o foco
txt_C.configure(state=DISABLED, yscrollcommand=scb2.set)  # configurando o status do txt_C

scb1.place(x=370, y=30)  # Definindo localização na tela pelo metodo pack do Tkinter
scb1.config(command=txt_CF.yview)  # Configurando o comando de scb1 para txt_CF

scb2.place(x=765, y=30)  # Definindo localização na tela pelo metodo pack do Tkinter
scb2.config(command=txt_C.yview)  # Configurando o comando de scb2 para txt_C

scb3.place(x=5, y=483)  # Definindo localização na tela pelo metodo pack do Tkinter
scb3.config(command=txt_CF.xview)  # Configurando o comando de scb1 para txt_CF

lb_CF.place(x=7, y=5)  # Definindo localização na tela pelo metodo place do Tkinter

lb_C.place(x=402, y=5)  # Definindo localização na tela pelo metodo place do Tkinter

bt_AL.place(x=10, y=530)  # Definindo localização na tela pelo metodo place do Tkinter

bt_AS.place(x=10, y=560)  # Definindo localização na tela pelo metodo place do Tkinter

bt_I.place(x=10, y=590)  # Definindo localização na tela pelo metodo place do Tkinter

bt_S.place(x=10, y=620)  # Definindo localização na tela pelo metodo place do Tkinter

# |Fim Configurando Instancias|


# LarguraxAltura+DistanticaEsqueda+DistanciaTopo
janela.geometry("800x650+300+10")  # Ajustando a Tela Principal
janela["bg"] = "#3c455c"  # Colocando a cor de fundo na tela principal
janela.resizable(0, 0)

janela.mainloop()  # Iniciando Tela Principal

