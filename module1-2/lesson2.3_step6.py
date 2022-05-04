import time
import time
import math

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    knop = browser.find_element_by_css_selector('[type = "submit"]')
    knop.click()
    browser.switch_to.window(browser.window_handles[1])
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
В этом задании после нажатия кнопки страница откроется в новой вкладке, 
нужно переключить WebDriver на новую вкладку и решить в ней задачу.
Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
 вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.


"""