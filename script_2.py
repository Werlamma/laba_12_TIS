from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)
browser.get('https://ru.pinterest.com/login')
time.sleep(3)
email_field = browser.find_element(By.ID, 'email')
email_field.send_keys('orlova.svetlana05@mail.ru')
password_field = browser.find_element(By.ID, 'password')
password_field.send_keys('Qwsazx34')
password_field.send_keys(Keys.ENTER)

time.sleep(5)
try:
    # Проверка наличия элемента, который указывает на успешную авторизацию
    avatar_svg = browser.find_element(By.CSS_SELECTOR, '[data-test-id="gestalt-avatar-svg"]')
    # Если элемент найден, считаем, что авторизация прошла успешно
    print('The test was completed successfully')
except NoSuchElementException:
    # Если элемент не найден, считаем, что авторизация не удалась
    print('The test was failed')
browser.quit()

#коректный вход