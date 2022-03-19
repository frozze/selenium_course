from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    fist_name = browser.find_element_by_name("firstname")
    fist_name.send_keys("Pavel")
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Frost")
    email = browser.find_element_by_name("email")
    email.send_keys("frozze@icloud.com")
    file = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'empty_file.txt')  # добавляем к этому пути имя файла
    file.send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
