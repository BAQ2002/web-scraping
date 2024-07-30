from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class WebDriverConfig:
    @staticmethod
    def config_chromedriver():
        # Configuração do driver
        service = Service(executable_path="chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.set_window_size(700, 800)
        return driver
