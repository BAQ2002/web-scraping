from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from links import links
from model.produto import Produto
from colorama import Fore, Style, init


# Inicializa o colorama
init(autoreset=True)


# Função para buscar informações de um produto
# Função para buscar informações de um produto
def fetch_product_info(driver, url):
    driver.get(url)

    # Verifica se a página de CAPTCHA está presente e faz refresh até que desapareça
    while True:
        try:
            captcha_present = driver.find_element(By.XPATH,
                                                  '//h4[contains(text(), "Digite os caracteres que você vê abaixo")]')
            if captcha_present:
                print(Fore.GREEN + "CAPTCHA detected, refreshing the page..." + Style.RESET_ALL)
                driver.refresh()
                time.sleep(2)  # Pausa para evitar sobrecarga do servidor
        except:
            # Se o CAPTCHA não estiver presente, prossegue com a extração das informações do produto
            break

    try:
        title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="productTitle"]'))
        ).text
    except Exception as e:
        print(Fore.RED + f"Error fetching title from URL {url}: {e}" + Style.RESET_ALL)
        return None

    try:
        price_whole = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'a-price-whole'))
        ).text
    except Exception as e:
        print(Fore.RED + f"Error fetching whole price from URL {url}: {e}" + Style.RESET_ALL)
        return None

    try:
        price_fraction = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="corePrice_feature_div"]/div/div/span[1]/span[2]/span[3]'))
        ).text
    except Exception as e:
        print(Fore.RED + f"Error fetching fractional price from URL {url}: {e}" + Style.RESET_ALL)
        return None

    price = f"{price_whole},{price_fraction}"

    return Produto(titulo=title, preco=price)


# Configuração do driver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Lista para armazenar os produtos
produtos = []

# Iterando sobre a lista de links e imprimindo as informações dos produtos
for url in links:
    product_info = fetch_product_info(driver, url)
    if product_info:
        produtos.append(product_info)
        print(product_info)
    time.sleep(2)  # Pausa para evitar problemas de carregamento

driver.quit()

# Exibindo a lista de produtos analisados
print("Lista de produtos analisados:")
for produto in produtos:
    print(Fore.BLUE + f'Name: {produto.titulo}\nR$:{produto.preco}\n' + Style.RESET_ALL)
