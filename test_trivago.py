import pytest  # Importa o pytest para criar e executar testes
from selenium import webdriver  # Importa o webdriver do Selenium para controlar o navegador
from selenium.webdriver.common.by import By  # Importa By para localizar elementos
from selenium.webdriver.common.keys import Keys  # Importa Keys para simular pressionamento de teclas
from selenium.webdriver.support.ui import WebDriverWait  # Importa WebDriverWait para esperar por condições específicas
from selenium.webdriver.support import expected_conditions as EC  # Importa expected_conditions para definir condições de espera

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Inicializa o ChromeDriver
    yield driver  # Fornece o driver para os testes
    driver.quit()  # Fecha o navegador após os testes

def test_trivago_search(browser):
    browser.get("http://www.trivago.com.br")  # Acessa o site do Trivago
    
    search_box = browser.find_element(By.ID, "input-auto-complete")  # Localiza o campo de busca pelo ID
    search_box.send_keys("Manaus")  # Digita "Manaus" no campo de busca
    search_box.send_keys(Keys.RETURN)  # Pressiona Enter para iniciar a busca
    
    # Espera até que os resultados sejam carregados
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".item__flex-column"))  # Espera até que o elemento com a classe especificada esteja presente
    )
    
    # Seleciona a opção "Avaliação e Sugestões"
    sort_dropdown = browser.find_element(By.ID, "mf-select-sortby")  # Localiza o dropdown de ordenação pelo ID
    sort_dropdown.click()  # Clica no dropdown
    sort_option = browser.find_element(By.XPATH, "//option[@value='7']")  # Localiza a opção de ordenação pelo valor
    sort_option.click()  # Seleciona a opção de ordenação
    
    # Verifica o nome, avaliação e valor do primeiro da lista
    first_item = browser.find_element(By.CSS_SELECTOR, ".item__flex-column")  # Localiza o primeiro item da lista pela classe
    name = first_item.find_element(By.CSS_SELECTOR, ".item__name").text  # Obtém o nome do primeiro item
    rating = first_item.find_element(By.CSS_SELECTOR, ".item__rating").text  # Obtém a avaliação do primeiro item
    price = first_item.find_element(By.CSS_SELECTOR, ".item__best-price").text  # Obtém o valor do primeiro item
    
    print(f"Nome: {name}")  # Imprime o nome do primeiro item
    print(f"Avaliação: {rating}")  # Imprime a avaliação do primeiro item
    print(f"Valor: {price}")  # Imprime o valor do primeiro item
    
    assert name is not None  # Verifica se o nome não é nulo
    assert rating is not None  # Verifica se a avaliação não é nula
    assert price is not None  # Verifica se o valor não é nulo
