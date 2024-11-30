from controller.scraper import Scraper
from model.produto import Produto
from colorama import Fore, Style
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time



# Implementação do scraper para Amazon
class AmazonScraper(Scraper):
    def fetch_product_info(self, url):
        self.driver.get(url)

        # Verifica se a página de CAPTCHA está presente e faz refresh até que desapareça
        while True:
            try:
                captcha_present = self.driver.find_element(By.XPATH, '//h4[contains(text(), "Digite os caracteres que você vê abaixo")]')
                if captcha_present:
                    print(Fore.GREEN + "CAPTCHA detected, refreshing the page..." + Style.RESET_ALL)
                    self.driver.refresh()
                    time.sleep(2)
            except:
                break

        try:
            title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="productTitle"]'))
            ).text
        except Exception as e:
            print(Fore.RED + f"Error fetching title from URL {url}: {e}" + Style.RESET_ALL)
            return None

        try:
            price_whole = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'a-price-whole'))
            ).text
            price_fraction = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'a-price-fraction'))
            ).text
            price_str = price_whole.replace('.', '') + '.' + price_fraction
            price = float(price_str)
        except Exception as e:
            print(Fore.RED + f"Error fetching price from URL {url}: {e}" + Style.RESET_ALL)
            return None

        return Produto(titulo=title, preco=price)



