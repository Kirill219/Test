from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_MonoPizza():

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://odesa.monopizza.com.ua/')
    browser.implicitly_wait(200)

    confirmCity = browser.find_element(By.LINK_TEXT,
                                       'Да, спасибо').click()
    section = browser.find_element(By.LINK_TEXT, 'Пицца').click()
    selectPizza = browser.find_element(By.LINK_TEXT,
                                       'Пицца 4 мяса').click()
    confirmPizza = browser.find_element(By.LINK_TEXT,
                                        'В корзину').click()
    cart = browser.find_element(By.LINK_TEXT,
                                'Корзина').click()

    result = browser.find_element(By.LINK_TEXT,
                                  '219 грн')

    assert result.tag_name == "div"
    assert result.text == "219 грн"

    browser.quit()