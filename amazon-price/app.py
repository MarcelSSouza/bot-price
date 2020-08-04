from selenium import webdriver
from selenium.webdriver.chrome.options import *
from os import *
from time import *
from smtplib import *

url=input("Digite a URL do produto no site da Amazon: ")
preco_desejado= input("Digite o preço que deseja pagar: ")
email_cliente= input("Digite o email que deseja receber as atualizações de preço: ")
driver=webdriver.Chrome()
driver.get(url)

sleep(5)
price= driver.find_element_by_xpath('//*[@id="price_inside_buybox"]')
price=price.text

print(f'Preço atual: {price}')

def send_email():
	smtp_email="___"
	smtp_password='____'
	server= smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login(smtp_email, smtp_password)

	subject="O preço do seu produto caiu!!!"
	body= f'O preço do seu produto acabou de diminuir no site da Amazon. Agora ele custa {price}'
	msg= f'Subject: {subject}\n\n\n{body}'

	server.send_email(
		smtp_email,
		email_cliente,
		msg
		)
	print("O seu email foi enviado com sucesso!!!")


send_email()

