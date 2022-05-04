import time
import math

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/alert_accept.html")
    knopka = browser.find_element_by_class_name("btn")
    knopka.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    def res(x):
      return math.log(abs(12*math.sin(x)))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(res(x))
    sub = browser.find_element_by_class_name('btn')
    sub.click()

finally:
    time.sleep(4)
    browser.quit()



"""
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
 вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.
"""