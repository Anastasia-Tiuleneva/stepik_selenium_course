from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time 
import math

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/find_link_text")
    link = browser.find_element_by_link_text("224592")
    link.click()
    input1 = browser.find_element_by_tag_name("input.form-control")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
