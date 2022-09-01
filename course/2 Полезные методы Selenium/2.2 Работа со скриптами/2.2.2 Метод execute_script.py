from selenium import webdriver
browser = webdriver.Chrome()
import time
try:
    browser.execute_script("document.title='Script executing'")


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(11)
    # закрываем браузер после всех манипуляций
    browser.quit()