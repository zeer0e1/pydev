import pyautogui
import pyautogui as escolha_opcao


def abrir_programa(prog):
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite(prog)
    escolha_opcao.press('Enter')
    escolha_opcao.sleep(3)
    escolha_opcao.press('Enter')


opcao = pyautogui.confirm('Clique no botão desejado', buttons=[
                          'Excel', 'word', 'notepad'])
if opcao == 'Excel':
    abrir_programa('excel')
elif opcao == 'word':
    abrir_programa('word')
elif opcao == 'notepad':
    abrir_programa('notepad')
