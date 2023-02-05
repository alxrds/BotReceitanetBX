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
    bot.press('tab')
    bot.press('tab')
    bot.press('down')
    bot.press('tab')
    bot.press('down')
    bot.press('tab')
    time.sleep(5)
    bot.write(cpf_cnpj)
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')
    bot.press('enter')
    time.sleep(5)
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')
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
        print("deu erro bora salvar CNPJ no arquivo")
        cnpj = [cpf_cnpj]
        with open('erro.csv', 'a') as csvfile:
            writer_object = writer(csvfile)
            writer_object.writerow(cnpj)
            csvfile.close() 
    else:
        print("Tudo certo bora pesquisar outro CNPJ")
    time.sleep(3)
    bot.hotkey('ctrl','w')