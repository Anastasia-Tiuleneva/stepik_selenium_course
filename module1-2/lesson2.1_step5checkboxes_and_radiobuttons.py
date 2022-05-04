#lesson2.1_step5
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time 
import math

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/math.html")
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(x))
    check1 = browser.find_element_by_id("robotCheckbox")
    check1.click()
    check2 = browser.find_element_by_id("robotsRule")
    check2.click()
    input2 = browser.find_element_by_class_name("btn")
    input2.click()


finally:
    time.sleep(7)
    browser.quit()


"""Ваша программа должна выполнить следующие шаги:

Открыть страницу http://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit."""