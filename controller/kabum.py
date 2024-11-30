from controller.scraper import Scraper
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from controller.links import links_kabum
from model.produto import Produto
from colorama import Fore, Style, init


# Inicializa o colorama
init(autoreset=True)


# Implementação do scraper para Kabum
class KabumScraper(Scraper):
    def fetch_product_info(self, url):
        self.driver.get(url)

        try:
            title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="container-purchase"]/div[1]/div/h1'))
            ).text
        except Exception as e:
            print(Fore.RED + f"Error fetching title from URL {url}: {e}" + Style.RESET_ALL)
            return None

        price_str = None
        try:
            # Primeiro XPath para o preço
            price_str = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="blocoValores"]/div[2]/div[1]/div/h4'))
            ).text
        except (TimeoutException, NoSuchElementException):
            try:
                # Segundo XPath para o preço
                price_str = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="blocoValores"]/div[3]/div[1]/div/h4'))
                ).text
            except (TimeoutException, NoSuchElementException) as e:
                print(Fore.RED + f"Error fetching price from URL {url}: {e}" + Style.RESET_ALL)
                return None

        try:
            price_str = price_str.replace('R$', '').replace('.', '').replace(',', '.').strip()
            price = float(price_str)
        except ValueError as e:
            print(Fore.RED + f"Error converting price from URL {url}: {e}" + Style.RESET_ALL)
            return None

        return Produto(titulo=title, preco=price)
