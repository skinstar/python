import requests
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

res = requests.get('http://www.doupan.com')
print(res.text)

# bor = Service(executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe')
driver = webdriver.Chrome()


class Service():
    def __init__(self,int):
        print(int)

    def _prepare(self, url):
        driver.get(url)
        driver.find_element(by=By.ID, value='key').send_keys('mac pro')
        btn = driver.find_element(by=By.XPATH, value='//*[@id="search"]/div/div[2]/button')
        btn.click()
        time.sleep(12)
        driver.quit()


if __name__ == '__main__':
    url = 'https://www.jd.com/'
    sc = Service(3);
    sc._prepare(url);
