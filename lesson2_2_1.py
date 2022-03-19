from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    x = num1.text
    num2 = browser.find_element_by_id("num2")
    y = num2.text
    answer = int(y) + int(x)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(answer))
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
