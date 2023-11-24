import xlsxwriter
import os

caminho_arquivo = "C:\\pydev\Controlando o computador\\Robo 2\moedas.xlsx"

planilha = xlsxwriter.Workbook(caminho_arquivo)
planilha1 = planilha.add_worksheet()
planilha1.write("A1", "Nome")
planilha.close()

os.startfile(caminho_arquivo)
