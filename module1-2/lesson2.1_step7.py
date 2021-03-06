#lesson2.1 step 7

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time 
import math

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element_by_tag_name("img")
    x = x_element.get_attribute("valuex")
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(x))
    check1 = browser.find_element_by_id("robotCheckbox")
    check1.click()
    check2 = browser.find_element_by_id("robotsRule")
    check2.click()
    submit = browser.find_element_by_tag_name("button")
    submit.click()



finally:
    time.sleep(7)
    browser.quit()




"""
В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. 
Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

Ваша программа должна:

Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.

 

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. 
Скопируйте его в поле ниже и нажмите кнопку "Submit", чтобы получить баллы за задание.
"""