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
#cadastrando os produtos
pyautogui.click()