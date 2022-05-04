from tabnanny import check
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time 
import math

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get("http://SunInJuly.github.io/execute_script.html")
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    def res(x):
      return math.log(abs(12*math.sin(x)))
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    input = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(res(x))
    chec = browser.find_element_by_id("robotCheckbox")
    chec.click()
    rad = browser.find_element_by_id("robotsRule")
    rad.click()
    sub = browser.find_element_by_class_name('btn')
    sub.click()

finally:
    time.sleep(4)
    browser.quit()




"""
Задание на execute_script
В данной задаче вам нужно будет снова преодолеть капчу для роботов и 
справиться с ужасным и огромным футером, который дизайнер всё никак не успевает переделать.
Вам потребуется написать код, чтобы:

Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), 
вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

Для этой задачи вам понадобится использовать метод execute_script, чтобы сделать прокрутку 
в область видимости элементов, перекрытых футером.
"""