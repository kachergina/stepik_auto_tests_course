from selenium import webdriver
from selenium.webdriver.common.by import By

#https://stepik.org/lesson/181384/step/7?unit=156009

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait2.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

#то, что вываливается ошибка - это правильное завершение теста, т.к. в уроке объясняют что за ошибка и как ее трактовать