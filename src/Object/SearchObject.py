from src.Setup import *
def searchBar():
    return driver.find_element(By.XPATH,'//input[@name="q"]')

def table():
    return driver.find_element(By.XPATH,"//table[@id='customers']")

def col():
    return driver.find_elements_by_xpath("//table[@id='customers']/tbody/tr[2]/td")