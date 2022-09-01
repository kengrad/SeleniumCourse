from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #находим элементы и вбиваем значения
    first_name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(2)")
    first_name.send_keys("Alexander")
    last_name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(4)")
    last_name.send_keys("Gal")
    email = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(6)")
    email.send_keys("123@gmail.com")

    #грузим файл
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '123.txt')           # добавляем к этому пути имя файла
    load = browser.find_element(By.ID,"file")
    load.send_keys(file_path)
    #submit
    submit = browser.find_element(By.CSS_SELECTOR,"body > div > form > button")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()