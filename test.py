from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_MonoPizza():

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://odesa.monopizza.com.ua/')
    browser.implicitly_wait(100)

    confirmCity = browser.find_element(By.XPATH,
                                       '//*[@id="main"]/div[3]/header/div/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/button[2]/span[1]').click()
    section = browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/header/div/div[1]/div[3]/div/div/a[2]').click()
    selectPizza = browser.find_element(By.XPATH,
                                       '//*[@id="main"]/main/div/div[2]/div[2]/div/div/div[1]/div[1]/span/img').click()
    confirmPizza = browser.find_element(By.XPATH,
                                        '//*[@id="main"]/main/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/button/span[1]').click()
    cart = browser.find_element(By.XPATH,
                                '//*[@id="main"]/div[3]/header/div/div[1]/div[1]/div/div[3]/a/div/img').click()

    result = browser.find_element(By.XPATH,
                                  '//*[@id="main"]/main/div/div[1]/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div')

    assert result.tag_name == "div"
    assert result.text == "219 грн"

    browser.quit()