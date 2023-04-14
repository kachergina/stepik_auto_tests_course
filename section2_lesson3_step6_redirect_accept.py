import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#https://stepik.org/lesson/184253/step/6?unit=158843

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

#Открыть страницу http://suninjuly.github.io/redirect_accept.html
#Нажать на кнопку
#Переключиться на новую вкладку
#Пройти капчу для робота и получить число-ответ

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "div .trollface")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, 'input_value').text
    x = calc(x_element)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(x)

    button2 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()