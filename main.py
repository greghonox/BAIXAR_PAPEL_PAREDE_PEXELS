"""
    GREGORIO HONORATO
    WHATSAPP: (19) 99250-9913
    TELEGRAM: @GREGHONO
    GREGHONO@GMAIL.COM
"""

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from os import getcwd, makedirs
from platform import platform
from requests import get
from time import sleep

BRR = '/' if 'windows' not in platform() else '\\'

class BaixarPexels:
    def __init__(self, caminho_papel_parede) -> None:
        URL = 'https://www.pexels.com/pt-br/procurar/4k%20paisagem%20wallpapers/'
        self.caminho_papel_parede = caminho_papel_parede
        self.dr = webdriver.Chrome()
        self.dr.get(URL)
        self.pegar_img()
        
    img_salva = []
    def pegar_img(self):
        while True:
            for img in self.dr.find_elements_by_tag_name('img'):
                try:
                    url = img.get_attribute('data-big-src')
                    name = img.get_attribute('alt')
                    
                    if name in self.img_salva: continue
                    
                    if url: self.baixar_img(url, name)
                except Exception as e: pass
            self.dr.find_element_by_tag_name('body').send_keys(Keys.END)
            sleep(5)
    
    def baixar_img(self, url, name):
        try: 
            print(f"BAIXANDO {name}")
            with open(self.caminho_papel_parede +BRR+ f"{name}.png", 'wb') as f: f.write(get(url).content)
        except Exception as e: print(f'ERRO OCORRIDO EM TENTAR BAIXAR {url} {e}')
    
    def __del__(self):
        self.dr.quit()
        self.dr.close()
        print(f'FINALIZANDO SCRIPT')

def criar_pasta():
    try: makedirs(getcwd() + BRR + 'imgs')
    except: pass
    
BaixarPexels(getcwd()+ BRR +'imgs')    