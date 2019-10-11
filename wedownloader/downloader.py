from selenium import webdriver
#from BeautifulSoup4 import BeautifulSoup
import pandas as pd
import requests
from lxml import html


driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

driver.get("http://care.srmist.edu.in/ktrds/")



for f in driver.forms():
    print(f)



usr = "RA1811003010182"
pswd ="rajat4563"


content = driver.page_source
soup = BeautifulSoup(content)