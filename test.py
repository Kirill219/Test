from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_MonoPizza():

    CHROME_OPTIONS = Options()
    CHROME_OPTIONS.add_experimental_option("detach", True)

    BROWSER = webdriver.Chrome(options=CHROME_OPTIONS)
    BROWSER.get('https://odesa.monopizza.com.ua/')
    BROWSER.implicitly_wait(200)

    confirm_city_button = BROWSER.find_element(By.LINK_TEXT,
                                       'Да, спасибо').click()
    select_section_button = BROWSER.find_element(By.LINK_TEXT, 'Пицца').click()
    select_pizza_button = BROWSER.find_element(By.LINK_TEXT,
                                       'Пицца 4 мяса').click()
    confirm_pizza_button = BROWSER.find_element(By.LINK_TEXT,
                                        'В корзину').click()
    select_cart_button = BROWSER.find_element(By.LINK_TEXT,
                                'Корзина').click()

    result_label = BROWSER.find_element(By.ID,
                                  'summary-prize')

    assert result_label.tag_name == "span"
    assert 'грн' in result_label.text

    BROWSER.quit()
