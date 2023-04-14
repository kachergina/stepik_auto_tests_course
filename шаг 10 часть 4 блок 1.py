import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#https://stepik.org/lesson/138920/step/11?unit=196194
# Это было ревью чего-то задания


link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    input3.send_keys("@yandex.ru")
    input4 = browser.find_element(By.CSS_SELECTOR,'input[placeholder="Input your phone:"]')
    input4.send_keys("880535")
    input5 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]')
    input5.send_keys("moskva")
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла