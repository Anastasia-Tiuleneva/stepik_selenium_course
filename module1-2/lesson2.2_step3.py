#lesson2.2 step 3

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time 
import math


try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/selects1.html")
    x_element = browser.find_element_by_id("num1")
    y_element  = browser.find_element_by_id("num2")
    x = int(x_element.text)
    y = int(y_element.text)
    def sum(x, y):
      return (x+y)
    z = str(sum(x, y))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(z)
    submit = browser.find_element_by_tag_name("button")
    submit.click()



finally:
    time.sleep(7)
    browser.quit()


"""
    Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов. 
Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), 
вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

 

Когда ваш код заработает, попробуйте запустить его на 
странице http://suninjuly.github.io/selects2.html. Ваш код и для нее тоже должен пройти успешно.
"""