import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

browser.get("http://suninjuly.github.io/explicit_wait2.html")

element_100= WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button = browser.find_element_by_id("book")
button.click()

def res(x):
      return math.log(abs(12*math.sin(x)))
x_element = browser.find_element_by_id("input_value")
x = int(x_element.text)
answer = browser.find_element_by_id("answer")
answer.send_keys(res(x))
sub = browser.find_element_by_id("solve")
sub.click()

"""
Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать 
нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, 
а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) 
и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, 
используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом. 
Отправьте его в качестве ответа на это задание.
"""