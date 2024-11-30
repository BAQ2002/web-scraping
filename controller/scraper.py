import time
from abc import ABC, abstractmethod
from colorama import Fore, Style

# Interface para Scraper
class Scraper(ABC):
    def __init__(self, driver):
        self.driver = driver
        self.produtos = []

    @abstractmethod
    def fetch_product_info(self, url):
        pass

    def scrape_products(self, links):
        for url in links:
            product_info = self.fetch_product_info(url)
            if product_info:
                self.produtos.append(product_info)
                print(Fore.YELLOW + f'{product_info}' + Style.RESET_ALL)
            time.sleep(2)  # Pausa para evitar problemas de carregamento

        self.driver.quit()

    def listar_produtos(self):
        print("\nLista de produtos analisados:")
        for produto in self.produtos:
            print(Fore.BLUE + f'Name: {produto.titulo}\nR$:{produto.preco}\n' + Style.RESET_ALL)

    def produtos_analisados(self):
        if not self.produtos:
            print('A lista de produtos está vazia.')
            return False
        else:
            return self.produtos
