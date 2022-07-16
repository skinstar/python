from lib2to3.pgen2 import driver
from msilib.schema import Class
import requests
from selenium import webdriver

driver = webdriver.Chrome("D:\soft\Python310\chromedriver.exe")
data = driver.get("https://www.jd.com")