from amazon import Amazon
from web_driver_config import WebDriverConfig


def main():
    # Configura o WebDriver
    driver = WebDriverConfig.config_chromedriver()

    # Cria uma instância da classe Amazon
    amazon_scraper = Amazon(driver)

    # Inicia o scraping de produtos
    amazon_scraper.scrape_products()

    # Listar produtos analidos no site Amazon.com.br
    amazon_scraper.listar_produtos()


if __name__ == '__main__':
    main()
