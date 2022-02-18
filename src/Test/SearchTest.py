from datetime import time
from src import Test
# from src.Setup import initial,final,time
from src.Page.SearchPage import *
# python -m src.Test.SearchTest

[Test]
def GoogleSearchTest():
    initial()
    driver.get('https://www.google.com/')
    GoogleSearch()
    time.sleep(3)
    final()

GoogleSearchTest()
[Test]
def GetTableDataTest():
    initial()
    GetTableData()
    final()
# GetTableDataTest()