from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pyautogui as gui
import xlsxwriter as excel
import os

caminho_arquivo = "C:\\pydev\Controlando o computador\\Robo 2\moedas.xlsx"
options = Options()
options.headless = True

moedas = ['Real', 'Dolar', 'Euro']
cotacoes = []

openBrowser = web.Chrome(service=Service('./chromedriver.exe'), options=options)

openBrowser.get("https://www.google.com.br")


def clean_search():
    openBrowser.find_element(By.NAME, 'q').send_keys("")
    gui.press('tab')
    gui.press('Enter')


def search(value):
    openBrowser.find_element(By.NAME, 'q').send_keys(value + ' HOJE')
    openBrowser.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
    value_now = openBrowser.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
    return value_now


for moeda in moedas:
    # search(moedas)
    try:
        new_cot = {moeda: search(moeda)}
        clean_search()
        cotacoes.append(new_cot)
    except:
        clean_search()
        continue


planilha_criada = excel.Workbook(caminho_arquivo)
planilha_moedas = planilha_criada.add_worksheet()
planilha_moedas.write('A1', 'Moeda')
planilha_moedas.write('B1', 'Valor')

formato_moeda = planilha_criada.add_format({'num_format': 'R$#,##0.00'})

celula = 2

for cotacao in cotacoes:
   for i, j in cotacao.items():
       planilha_moedas.write(f'A{celula}', i, formato_moeda)
       planilha_moedas.write(f'B{celula}', j, formato_moeda)
       celula +=1

planilha_criada.close()


os.startfile(caminho_arquivo)