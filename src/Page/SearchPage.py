from src.Object.SearchObject import *

def GoogleSearch():
    searchBar().send_keys("hello")
    # searchBar(Keys.Enter)
def GetTableData():
    row = table().find_elements(By.TAG_NAME,"tr")
    for r in row:
        col = r.find_elements(By.TAG_NAME,"td")
        for c in col:
            cell = c.text
            if cell=="Germany":
                print("Pass")
