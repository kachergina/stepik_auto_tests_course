#Открыть страницу http://suninjuly.github.io/file_input.html
##Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
#Нажать кнопку "Submit".
#https://stepik.org/lesson/228249/step/8?unit=200781

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('Galina')
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys('Kochergina')
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys('g@mail.ru')

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'lesson2_2_step8.docx')
    file_btn = browser.find_element(By.ID, "file")
    file_btn.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()