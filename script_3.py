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
email_field.send_keys('orlovasvetalana164@gmail.com')
password_field = browser.find_element(By.ID, 'password')
password_field.send_keys('Qwsazx34')
password_field.send_keys(Keys.ENTER)
time.sleep(5)

search_box = browser.find_element(By.CSS_SELECTOR, '[data-test-id="search-box-input"]')

search_box.clear()

search_box.send_keys('Дом')

search_box.send_keys(Keys.ENTER)

time.sleep(4)

image = browser.find_element(By.CSS_SELECTOR, '[aria-label="Страница пина «Каменный современный дом»"]')

image.click()

time.sleep(4)

save_button = browser.find_element(By.CSS_SELECTOR, 'button[aria-label="Сохранить"]')
save_button.click()

time.sleep(4)

try:

    # Проверка наличия элемента, который указывает на успешную авторизацию
    avatar_svg = browser.find_element(By.CSS_SELECTOR, '[data-test-id="gestalt-avatar-svg"]')

    # Если элемент найден, считаем, что авторизация прошла успешно
    print('The test was completed successfully')
except NoSuchElementException:
    # Если элемент не найден, считаем, что авторизация не удалась
    print('The test was failed')
browser.quit()

#сохранение фотографии в личный кабинет