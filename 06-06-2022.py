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
    inbox = browser.find_element(By.CSS_SELECTOR, '[data-test="link-conversation"]')
    inbox.click()
    time.sleep(10)
    assert browser.current_url == 'https://cpstaging.snatch.cloud/conversation', 'NOT Inbox'

    # reports
    reports = browser.find_element(By.CSS_SELECTOR, '[data-test="link-reports"]')
    reports.click()
    time.sleep(10)
    assert browser.current_url == 'https://cpstaging.snatch.cloud/reports', 'NOT Reports'

    # nlp
    nlp = browser.find_element(By.CSS_SELECTOR, '[data-test="link-nlp"]')
    nlp.click()
    time.sleep(5)
    assert browser.current_url == 'https://cpstaging.snatch.cloud/nlp', 'NOT NLP'

    # charts
    charts = browser.find_element(By.CSS_SELECTOR, '[data-test="link-charts"]')
    charts.click()
    time.sleep(5)
    decline = browser.find_element(By.CSS_SELECTOR, '[id="hs-eu-decline-button"]')
    decline.click()
    assert browser.current_url == 'https://cpstaging.snatch.cloud/charts', 'NOT Advanced Stats'

    # profile
    profile = browser.find_element(By.CSS_SELECTOR, '[data-test="profile_router_link"]')
    profile.click()
    time.sleep(5)
    assert browser.current_url == 'https://cpstaging.snatch.cloud/profile', 'NOT Profile'

    # profile_payment_system
    payment = browser.find_element(By.CSS_SELECTOR, '[data-test="profile_payment_router_link"]')
    payment.click()
    time.sleep(2)
    assert browser.current_url == 'https://cpstaging.snatch.cloud/profile/payment', 'NOT Payment System'