from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    x1_element = browser.find_element(By.ID, "num1")  # первый элемент
    x1 = x1_element.text
    x2_element = browser.find_element(By.ID, "num2")  # 2
    x2 = x2_element.text
    sum = str(int(x1)+int(x2))

    select = Select(browser.find_element(By.ID, "dropdown"))  # выбрать выпадающий список
    select.select_by_value(sum)  # ищем элемент с суммой

    submit = browser.find_element(By.CSS_SELECTOR,"body > div > form > button")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
