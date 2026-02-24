import time

def test_home(browser):
    url = "http://127.0.0.1:9090"
    browser.get(url)
    time.sleep(10)
    assert browser.title == "Dash"
    print("Teste da pagina inicial concluído com sucesso.")
