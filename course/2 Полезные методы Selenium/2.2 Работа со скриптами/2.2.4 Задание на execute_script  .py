from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

#находим элемент и выполняем вычисления
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

#вбиваем ответ
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
#чекбокс
    checkRobot = browser.find_element(By.ID, "robotCheckbox")
    checkRobot.click()
#радиобаттон
    radioRobot = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radioRobot)
    radioRobot.click()
#submit
    submit = browser.find_element(By.CSS_SELECTOR,"body > div > form > button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()