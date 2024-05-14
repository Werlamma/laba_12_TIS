from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)
browser.get('https://ru.pinterest.com/login')
time.sleep(3)
email_field = browser.find_element(By.ID, 'email')
email_field.send_keys('email')
password_field = browser.find_element(By.ID, 'password')
password_field.send_keys('SSSSSSS')
password_field.send_keys(Keys.ENTER)
time.sleep(5)

browser.quit()

#Некоректный вход