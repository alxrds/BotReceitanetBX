#800x600
#print(bot.position())

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

df = pd.read_csv('cnpj.csv')

def insere_tab(number):
    count = 0
    while (count < number):
        bot.press('tab')                            
        count += 1

for i in range(len(df.index)):
    cpf_cnpj = str(df.iloc[i,0])

    if len(cpf_cnpj) == 13:
        cpf_cnpj = '0' + str(cpf_cnpj)

    print('Iniciando Tarefa CNPJ ' + str(cpf_cnpj))
    time.sleep(3)
    bot.press('win')
    time.sleep(3)
    bot.write('Receitanet BX')
    time.sleep(3)
    bot.press('enter')
    time.sleep(6)
    insere_tab(2)
    bot.press('down')
    bot.press('tab')
    bot.press('down')
    bot.press('tab')
    time.sleep(2)
    bot.write(cpf_cnpj)
    time.sleep(2)
    insere_tab(4)
    time.sleep(1)
    bot.press('enter')  
    time.sleep(3)
    insere_tab(8)
    bot.press('down')
    bot.press('tab')
    bot.press('down')
    time.sleep(1)
    bot.click(606, 260)
    time.sleep(1)
    bot.click(468, 302)
    time.sleep(1)
    bot.click(305, 308)
    time.sleep(1)
    bot.write('010223')
    time.sleep(1)
    bot.click(305, 326)
    time.sleep(2)
    bot.write('280223')
    time.sleep(1)
    bot.press('tab')
    time.sleep(1)
    bot.hotkey('ctrl','p')
    time.sleep(3)
    bot.press('enter')
    time.sleep(3)
    bot.click(522, 551)
    bot.hotkey('ctrl','a')
    time.sleep(2)
    bot.hotkey('ctrl','c')
    root = Tk()
    root.withdraw()
    texto = root.clipboard_get()
    texto_formatado = texto.upper()
    time.sleep(3)
    
    if("NÃO" in texto_formatado):
        print("Erro! Salvando CNPJ no arquivo.")
        cnpj = [cpf_cnpj]
        with open('erro.csv', 'a') as csvfile:
            writer_object = writer(csvfile)
            writer_object.writerow(cnpj)
            csvfile.close()
        print("CNPJ salvo.") 
        
    time.sleep(3)
    bot.hotkey('enter')
    bot.hotkey('ctrl','w')
    bot.hotkey('ctrl','w')