from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # click button
    button = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    button.click()

    #переход в другую вкладку
    second_window = browser.window_handles[1]
    first_window = browser.window_handles[0] #в рамках задачи это не нужно, запись в переменную 1й вкладки
    browser.switch_to.window(second_window)

    # решение капчи
    x1 = browser.find_element(By.ID, "input_value")
    x = x1.text
    y = calc(x)

    # вводим решение
    answer = browser.find_element(By.ID,"answer")
    answer.send_keys(y)

    #подтверждение click button
    submit = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
