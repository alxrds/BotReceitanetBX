import pyautogui as bot
from tkinter import Tk
import time
import datetime
from csv import writer
import pandas as pd

data_atual = datetime.datetime.now()
mes_atual = data_atual.strftime("%m")
mes_pesquisa = int(mes_atual) - 2
ano_atual = data_atual.strftime("%y")
ano_pesquisa = int(ano_atual)

if(mes_pesquisa == 0):
    mes_pesquisa = 12
    ano_pesquisa -= 1

df = pd.read_csv('cnpj.csv')
data_inicial = '01' + str(mes_pesquisa) +''+ str(ano_pesquisa)
data_final = '31' + str(mes_pesquisa) +''+ str(ano_pesquisa)

def insere_tab(number):
    count = 0
    while (count < number):
        bot.press('tab')                            
        count += 1

for i in range(len(df.index)):
    cpf_cnpj = str(df.iloc[i,0])
    print('Iniciando Tarefa CNPJ ' + str(cpf_cnpj))
    time.sleep(3)
    bot.press('win')
    time.sleep(3)
    bot.write('Receitanet BX')
    time.sleep(3)
    bot.press('enter')
    time.sleep(5)
    insere_tab(2)
    bot.press('down')
    bot.press('tab')
    bot.press('down')
    bot.press('tab')
    time.sleep(3)
    bot.write(cpf_cnpj) 
    time.sleep(3)
    insere_tab(4)
    time.sleep(5)
    bot.press('enter')  
    time.sleep(5)
    insere_tab(8)
    bot.press('down')
    bot.press('tab')
    bot.press('down')
    time.sleep(3)
    bot.click(956, 278)
    time.sleep(3)
    bot.click(762, 323)
    time.sleep(3)
    bot.write(data_inicial)
    bot.press('down')
    time.sleep(3)
    bot.write(data_final)
    bot.press('tab')
    time.sleep(3)
    bot.hotkey('ctrl','p')
    time.sleep(10)
    bot.press('enter')
    bot.click(869, 700)
    bot.hotkey('ctrl','a')
    time.sleep(2)
    bot.hotkey('ctrl','c')
    root = Tk()
    root.withdraw()
    texto = root.clipboard_get()
    texto_formatado = texto.upper()
    time.sleep(3)
    if("NENHUM" in texto_formatado):
        print("Deu erro! bora salvar CNPJ no arquivo e ir para o proxímo caso exista")
        cnpj = [cpf_cnpj]
        with open('erro.csv', 'a') as csvfile:
            writer_object = writer(csvfile)
            writer_object.writerow(cnpj)
            csvfile.close()
        print("CNPJ salvo no arquivo, bora para o proxímo caso exista") 
    else:
        print("Tudo certo! Se existir bora pesquisar outro CNPJ")
    time.sleep(3)
    bot.hotkey('ctrl','w')