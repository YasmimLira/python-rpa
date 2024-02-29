from selenium import webdriver as webdriver
from selenium.webdriver.common.by import By
import pyautogui as action
import pyautogui as loadTime

navegadorFake = webdriver.Chrome()

navegadorFake.get('https://totvs-torres.monday.com/')

loginInput = navegadorFake.find_element(By.ID, 'user_email').send_keys('teste@gmail.com')
passwordInput = navegadorFake.find_element(By.ID, 'user_password').send_keys('11111111')
loadTime.sleep(2)

loginButton = navegadorFake.find_element(By.CLASS_NAME, 'next-button-component').click()
loadTime.sleep(10)

poolServicesButton = navegadorFake.find_element(By.CLASS_NAME, 'text-with-highlights').click()
loadTime.sleep(3)
testButton = True
if testButton:
    tpfButton = navegadorFake.find_element(By.CLASS_NAME, 'L0jfS').click()
if testButton:
    tpfButton = navegadorFake.find_element(By.CLASS_NAME, 'mcvR3').click()
loadTime.sleep(5)
optionButton = navegadorFake.find_element(By.CLASS_NAME, 'referenceWrapper_d8c3da695b').click()
loadTime.sleep(4)

texto_alvo = "Mais ações"
elemento = navegadorFake.find_element(By.XPATH, f'//*[text()="{texto_alvo}"]').click()

loadTime.sleep(3)

text_excel = "Exportar quadro para o Excel"
excelButton = navegadorFake.find_element(By.XPATH, f'//*[text()="{text_excel}"]').click()
loadTime.sleep(3)

textCheckbox = "Incluir Subelementos"
checkBoxButton = navegadorFake.find_element(By.XPATH, f'//*[text()="{textCheckbox}"]').click()
loadTime.sleep(2)

sendButton = navegadorFake.find_element(By.XPATH, '/html/body/div[55]/div/div/div/div/div/div/div[3]/button').click()

loadTime.sleep(10)
