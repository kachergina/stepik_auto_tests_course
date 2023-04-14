from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

#https://stepik.org/lesson/165493/step/7?unit=140087


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    treasure_element = browser.find_element(By.ID, 'treasure')
    treasure_value = treasure_element.get_attribute('valuex')
    print("value of treasure: ", treasure_value)
    x = treasure_value
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()