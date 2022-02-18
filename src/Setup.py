import time
import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = Chrome("F:\Downloads\chromedriver_win32\chromedriver.exe")
# driver = Chrome(ChromeDriverManager().install())


def initial():
    driver.implicitly_wait(10)
    driver.get('https://www.w3schools.com/html/html_tables.asp')
    # driver.switch_to.frame(driver.find_element(By.NAME,"Login"))
    # username = driver.find_element(By.ID,"loginLoginId")
    # username.send_keys("hello")
    # time.sleep(3)
    # return final()

def final():
    driver.quit()


# initial()
