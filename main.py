from amazon import Amazon
from web_driver_config import WebDriverConfig
from controller.database import DatabaseManager


def main():
    # Configura o WebDriver
    driver = WebDriverConfig.config_chromedriver()

    # Cria uma instância da classe Amazon
    amazon_scraper = Amazon(driver)

    # Inicia o scraping de produtos
    amazon_scraper.scrape_products()

    # Listar produtos analidos no site Amazon.com.br
    amazon_scraper.listar_produtos()

    # Recupera os produtos analisados
    produtos = amazon_scraper.produtos_analisados()

    if produtos:
        # Salva os produtos no banco de dados
        db_manager = DatabaseManager()
        for produto in produtos:
            db_manager.salvar_produto(produto)
        db_manager.fechar()


if __name__ == '__main__':
    main()
