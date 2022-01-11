import os
from tkinter import *
import tkinter as tk


janela = tk.Tk()

def traco():
    print('-'*70)


#____________________________________________________________________
#INFORMAÇÕES INICIAIS



janela.title('Renamer Book v.1.2')
janela.geometry('600x400')

nomerb = Label(janela, text="RENAMER BOOK - VERSÃO 1.2 - 2019")
nomerb.place(x=150, y=25)

desgui = Label(janela, text="Criado por Guilherme Micheletti")
desgui.place(x=170, y=50)


#____________________________________________________________________
#INSTRUÇÕES


frase1 = Label(janela, text="Para que o Renamer Book funcione, a lista deverá seguir a seguinte estrutura:")
frase1.place(x=50, y=100)

frase2 = Label(janela, text="nomeoriginal.extensão + ponto e vígula + novonome.extensão")
frase2.place(x=80, y=120)

frase3 = Label(janela, text="EX: IMG2589.jpg;guilherme-micheletti-mc-IMG2589.jpg")
frase3.place(x=100, y=140)




#____________________________________________________________________
#SEPARAR
def bt_click_separar():
    traco()
    print ('Movendo Fotos...')
    traco()
    import os.path
    import shutil

    arq = open('_RENAMER_BOOK_lista.txt', 'r')
    dir_arquivo = ''

    for linha in arq:
    
        nomeantigo, novonome = linha.rstrip().split(';')
        dir_arquivo = os.path.dirname(nomeantigo)

        if  os.path.isdir('./COMPLETO'): # verifica se este diretorio ja existe
            print ('-')
        else:
            os.mkdir('./COMPLETO') # criar a pasta caso não exista
            print ('Pasta criada com sucesso!')

        if os.path.isfile(nomeantigo): # verifica se arquivo existe
            print ()
        else:
            print (' ')
            print (' ')
            print ('***ALERTA BOOK*** O arquivo do formando não está na pasta ----> ' , nomeantigo )
            print (' ')
            print (' ')
            lbseparar1 = Label(janela, text="***ALERTA BOOK*** Algum arquivo não está na pasta ou já foi movido.")
            lbseparar1.place(x=60, y=300)
         
            continue
        
        tamanho = os.path.getsize(nomeantigo)/1024/1024        
        if (tamanho>=2):#2MB
            shutil.move(nomeantigo,'./COMPLETO')
        else: 
            print (' ')
            print (' ')
            print ('***ALERTA BOOK*** Arquivo com baixa qualidade. Será movido para para .PENDENTE ----> ' , nomeantigo )
            print (' ')
            print (' ')
            if  os.path.isdir('./PENDENTE')==False:
                os.mkdir('./PENDENTE')
            shutil.move(nomeantigo,'./PENDENTE')            

        print (nomeantigo, 'Movido')

        
        lbseparar2 = Label(janela, text="Arquivos separados!")
        lbseparar2.place(x=80, y=280)

#____________________________________________________________________
#RENOMEAR

def bt_click_renomear():
    
    traco()
    print('Renomeando Fotos...')
    traco()
    
                   
    arq = open('./_RENAMER_BOOK_lista.txt', 'r')
    os.chdir('COMPLETO')

    for linha in arq:
        nomeantigo, novonome = linha.rstrip().split(';')
        novonome = novonome.lower()
        novonome = novonome.replace(' ','-')
        novonome = novonome.replace('_','-')
        novonome = novonome.replace('- ','-')
        novonome = novonome.replace('-- ','-')
        novonome = novonome.replace('--','-')
        novonome = novonome.replace('---','-')
        novonome = novonome.replace('----','-')
        novonome = novonome.replace('ç','c')
        novonome = novonome.replace('á','a')
        novonome = novonome.replace('ã','a')
        novonome = novonome.replace('â','a')
        novonome = novonome.replace('é','e')
        novonome = novonome.replace('ê','e')
        novonome = novonome.replace('í','i')
        novonome = novonome.replace('ó','o')
        novonome = novonome.replace('ô','o')
        novonome = novonome.replace('ú','u')
        novonome = novonome.replace('meio-corpo','mc')
        novonome = novonome.replace('corpo-inteiro','ci')

        
        dir_arquivo = os.path.dirname(novonome)
       

        

        if os.path.isfile(nomeantigo): # verifica se arquivo existe
            print ('-')
        else:
            print (' ')
            print (' ')
            print ('***ALERTA BOOK*** O arquivo não está na pasta -------> ' , nomeantigo )
            print (' ')
            print (' ')
            lbrenomear1 = Label(janela, text="***ALERTA BOOK*** Algum arquivo não está na pasta ou já foi renomeado.")
            lbrenomear1.place(x=50, y=320)
            continue
         
        

        os.rename(nomeantigo, novonome)
        print(f'Arquivo {nomeantigo} renomeado para {novonome}')

        lbrenomear2 = Label(janela, text="Arquivos renomeados!")
        lbrenomear2.place(x=80, y=320)

    
        
#____________________________________________________________________
#BOTOES

btseparar = Button(janela, width=20, text='Separar', command=bt_click_separar)
btseparar.place(x=100, y=200)



btrenomear = Button(janela, width=20, text='Renomear', command=bt_click_renomear)
btrenomear.place(x=290, y=200)

#____________________________________________________________________




janela.mainloop()
