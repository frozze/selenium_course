from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    textBox = browser.find_element_by_id("answer")
    textBox.send_keys(y)
    checkBox = browser.find_element_by_id("robotCheckbox")
    checkBox.click()
    radioRobot = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true)", radioRobot)
    radioRobot.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
