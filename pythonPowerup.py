import pyautogui
import pandas
import time

pyautogui.PAUSE = 0.5

#entrando no google
pyautogui.press("win")

pyautogui.write("Google")

pyautogui.press("enter")

#entrando no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")
time.sleep(3)

#fazendo login
pyautogui.click(x=533, y=390)
pyautogui.write("email374@gmai.com")
pyautogui.press("tab")
pyautogui.write("Senhasupersecretaqueeufizusandopython")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)


#importando base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)


#cadastrando os produtos e automatizando o processo
for linha in tabela.index:
    pyautogui.click(x=554, y=269) #clicando no campo
    cod = tabela.loc[linha, 'codigo']
    pyautogui.write(cod)

    pyautogui.press("tab") #passando para o proximo campo
    marca =tabela.loc[linha, 'marca']
    pyautogui.write(marca)

    pyautogui.press("tab") #passando para o proximo campo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)

    pyautogui.press("tab") #passando para o proximo campo
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)

    pyautogui.press("tab") #passando para o proximo campo
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write('R$'+preco)

    pyautogui.press("tab") #passando para o proximo campo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write('R$'+custo)

    pyautogui.press("tab") #passando para o proximo campo
 
    obs = str(tabela.loc[linha, 'obs'])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab") #clicando no botão para enviar
    pyautogui.press("enter")

    pyautogui.scroll(1000) # voltando para o topo da pagina

