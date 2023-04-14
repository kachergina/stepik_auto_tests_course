from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#https://stepik.org/lesson/181384/step/5?unit=156009

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")

#time.sleep(1)
button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text