import pandas as pd #pandas, selenium, xlrd, openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import urllib

contatos_df = pd.read_excel("Enviar.xlsx")
#print(contatos_df)

navegador = webdriver.Chrome('chromedriver') #abrindo o navegador
navegador.get("https://web.whatsapp.com/") # abrindo o link

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

# Login já foi feito

for i, mensagem in enumerate (contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Numero"]
    texto  = urllib.parse.quote(f" Oi {pessoa} ! {mensagem} Esta é uma mensagem de teste automatizado !")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)    
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)
        