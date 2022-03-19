from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    textBox = browser.find_element_by_css_selector("#answer")
    textBox.send_keys(y)
    checkBox = browser.find_element_by_id("robotCheckbox")
    checkBox.click()
    radioRobot = browser.find_element_by_id("robotsRule")
    radioRobot.click()
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
