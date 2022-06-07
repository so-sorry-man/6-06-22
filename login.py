import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

browser = webdriver.Chrome()
browser.maximize_window()

# проверка логина с валидными данными (пользователь подтвердил регистрацию)
def test_login_1():
    browser.get('https://staging.snatch.cloud/')
    browser.find_elements(By.CLASS_NAME, 'button--log-in')[1].click()
    input_email = browser.find_element(By.CSS_SELECTOR, '[data-test="login_email_input"]')
    input_email.send_keys("nosokina@zuzex.com")
    input_password = browser.find_element(By.CSS_SELECTOR, '[data-test="login_password_input"]')
    input_password.send_keys('111111')
    login = browser.find_element(By.CSS_SELECTOR, '[data-test="sign_in_btn"]')
    login.click()
    decline = browser.find_element(By.CSS_SELECTOR, '[id="hs-eu-decline-button"]')
    decline.click()
    time.sleep(5)
    logout = browser.find_element(By.LINK_TEXT, "Выйти")
    logout.click()
    time.sleep(5)

# проверка логина с невалидным паролем (пользователь подтвердил регистрацию)
def test_login_2():
    input_email = browser.find_element(By.CSS_SELECTOR, '[data-test="login_email_input"]')
    input_email.send_keys("nosokina@zuzex.com")
    input_password = browser.find_element(By.CSS_SELECTOR, '[data-test="login_password_input"]')
    input_password.send_keys('111171')
    login = browser.find_element(By.CSS_SELECTOR, '[data-test="sign_in_btn"]')
    login.click()
    # ниже какой-то косяк
    # invalidok = browser.find_element(By.CSS_SELECTOR, '[data-test="btn-alert-modal2"]')
    # invalidok.click()
    # assert browser.current_url == 'https://cpstaging.snatch.cloud/login', 'NOT Login Page'