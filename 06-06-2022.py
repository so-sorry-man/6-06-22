import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()


def test_login():
    browser.get('https://staging.snatch.cloud/')
    browser.find_elements(By.CLASS_NAME, 'button--log-in')[1].click()
    input_email = browser.find_element(By.CSS_SELECTOR, '[data-test="login_email_input"]')
    input_email.send_keys("nosokina@zuzex.com")
    input_password = browser.find_element(By.CSS_SELECTOR, '[data-test="login_password_input"]')
    input_password.send_keys('111111')
    login = browser.find_element(By.CSS_SELECTOR, '[data-test="sign_in_btn"]')
    login.click()
    time.sleep(5)

    # dashboard
    assert browser.current_url == 'https://cpstaging.snatch.cloud/dashboard', 'NOT Dashboard'
    assert browser.title == 'Обзор - SnatchBot (dev)'

    #my_bots
    mybots = browser.find_element(By.CSS_SELECTOR, '[data-test="route-bots"]')
    mybots.click()
    time.sleep(3)
    assert browser.current_url == 'https://cpstaging.snatch.cloud/bots', 'NOT My Bots'

    #plugins
    plugins = browser.find_element(By.CSS_SELECTOR, '[data-test="plugins_router_link"]')
    plugins.click()
    time.sleep(3)
    assert browser.current_url == 'https://cpstaging.snatch.cloud/plugins', 'NOT Plugins'

    # inbox

