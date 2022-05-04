import os
from time import time
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/file_input.html")
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Alla")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Pugacheva")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("qwe@ya.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    file = browser.find_element_by_id("file")
    file.send_keys(file_path)
    sub = browser.find_element_by_class_name('btn')
    sub.click()

finally:
    time.sleep(4)
    browser.quit()





"""
Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
"""