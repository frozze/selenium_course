from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/math.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    textBox = browser.find_element_by_css_selector("#answer")
    textBox.send_keys(y)
    checkBox = browser.find_element_by_css_selector("label[for='robotCheckbox']")
    checkBox.click()
    radioRobot = browser.find_element_by_css_selector("label[for='robotsRule']")
    radioRobot.click()
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
