from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = "Olá, boa noite. Como posso ajuda-lo?"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["Grupo 1", "Grupo 2", "Grupo 3"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedrive.exe', chrome_options=options)

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(20)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element("xpath", 
                f"//span[@title='{grupo_ou_pessoa}']")
            time.sleep(1)
            campo_grupo.click()
            chat_box = self.driver.find_element(By.CLASS_NAME, '_3Uu1_')
            time.sleep(1)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element("xpath", 
                "//span[@data-icon='send']")
            time.sleep(1)
            botao_enviar.click()
            time.sleep(15)


bot = WhatsappBot()
bot.EnviarMensagens()