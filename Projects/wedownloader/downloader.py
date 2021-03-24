from selenium import webdriver
#from BeautifulSoup4 import BeautifulSoup
import pandas as pd
import requests
from lxml import html


driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

driver.get("website")



for f in driver.forms():
    print(f)



usr = "username"
pswd ="pass"


content = driver.page_source
soup = BeautifulSoup(content)
