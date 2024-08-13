# Projeto de Web Scraping

Este projeto realiza web scraping de produtos em sites como Amazon e KaBuM!, analisando os preços e verificando se algum produto atingiu o preço alvo. Os resultados são armazenados em um banco de dados para futuras análises.

## Estrutura do Projeto

- `controller/amazon.py`: Classe responsável por realizar o scraping de produtos da Amazon.
- `controller/kabum.py`: Classe responsável por realizar o scraping de produtos da KaBuM!.
- `web_driver_config.py`: Configuração do WebDriver para automação do navegador.
- `model/database.py`: Gerenciamento de operações com o banco de dados.

## Funcionalidades

- **Scraping de Produtos**: Extração de informações de produtos dos sites Amazon e KaBuM!.
- **Análise de Preços**: Verificação do menor preço do dia e análise de preços alvo.
- **Armazenamento em Banco de Dados**: Os dados extraídos são salvos em um banco de dados para futuras consultas.

## Pré-requisitos

- Python 3.6 ou superior
- Google Chrome e ChromeDriver compatível
- Banco de dados configurado