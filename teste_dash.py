import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def criar_driver():
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service("/usr/bin/chromedriver")

    return webdriver.Chrome(service=service, options=chrome_options)

def test_paginas_dash():
    url = "http://127.0.0.1:9090"

    driver = criar_driver()

    driver.get(url)
    time.sleep(2)
    assert "Dashboard" in driver.title

    driver.get(url + "/Formulário")
    time.sleep(2)
    assert "Formulário" in driver.page_source

    driver.get(url + "/Gráficos")
    time.sleep(2)
    assert "Gráficos" in driver.page_source

    driver.quit()
