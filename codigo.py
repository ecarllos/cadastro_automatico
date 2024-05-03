# passo - 1 entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip install pyautogui
import pyautogui
import time
# clicar -> pyautogui.click
# escrever -> pyautogui.write("")
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey
pyautogui.PAUSE = 0.5

pyautogui.press("win")

pyautogui.write("opera")

pyautogui.press("enter")
time.sleep(3)
# passo - 2 fazer login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)
#digitar o email
pyautogui.click(x=523, y=387)
pyautogui.write("ecarllos987@gmail.com")

#digitar a senha
pyautogui.press("tab")

pyautogui.write("bombomebom")

#avançar
pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.press("tab")
# passo - 3 importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")


# passo - 4 cadastrar um produto
#código do produto

for linha in tabela.index:
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    #marca do produto
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo do produto
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria do produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preco do produto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo do produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #observações
    obs = tabela.loc[linha, "obs"]    
    if not pandas.isna(obs):tho
    pyautogui.write(obs)
    pyautogui.press("tab")
    #ENVIAR
    pyautogui.press("enter")
# passo - 5 repetir esse processo até acabar com a base de dados


