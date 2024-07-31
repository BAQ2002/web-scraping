from controller.amazon import Amazon
from web_driver_config import WebDriverConfig
from model.database import DatabaseManager


def analise_de_precos(produtos):
    # Abalisa os precos e seus comportamentos
    db_manager = DatabaseManager()

    # Busca o menor preço do dia
    db_manager.buscar_menor_preco_dia(produtos)

    # Verifica se algum produto atingiu o preço alvo apos o
    db_manager.executa_verificacao_de_preco_alvo(produtos)

    db_manager.fechar()


def main():
    # Configura o WebDriver
    driver = WebDriverConfig.config_chromedriver()

    # Cria uma instância da classe Amazon
    amazon_scraper = Amazon(driver)

    # Inicia o scraping de produtos
    amazon_scraper.scrape_products()

    # Recupera os produtos analisados
    produtos = amazon_scraper.produtos_analisados()

    # Salva os produtos no banco de dados
    if produtos:
        db_manager = DatabaseManager()
        for produto in produtos:
            db_manager.salvar_produto(produto)
        db_manager.fechar()

    analise_de_precos(produtos)


if __name__ == '__main__':
    main()
