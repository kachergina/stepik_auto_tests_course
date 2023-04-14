from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math
import time


#https://stepik.org/lesson/228249/step/3?unit=200781

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

# Получаем со траницы первое число
    num1 = browser.find_element(By.ID, 'num1').text

# Получаем со траницы второе число
    num2 = browser.find_element(By.ID, 'num2').text

# Считаем сумму чисел
    sum_of_nums = int(num1) + int(num2)

# Находим элемент dropdown
    select = Select(browser.find_element(By.ID, 'dropdown'))

# Выбираем пункт dropdown'а, свойтво value, которого соответствует сумме
    select.select_by_value(str(sum_of_nums))

# Можно было бы выбрать нужный элемент так:
# select = Select(driver.find_element_by_css_selector('#dropdown'))
# select.select_by_visible_text(str(sum_of_nums))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()