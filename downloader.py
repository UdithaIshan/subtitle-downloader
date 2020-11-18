from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import re

CHROMEDRIVER_PATH = "C:/Windows/chromedriver.exe"
fileList = os.listdir()
regex = re.compile(".*\.(mp4|avi|flv|mkv|mov|wmv)$")

def newChromeBrowser(headless=True, downloadPath=None):
    """ Helper function that creates a new Selenium browser """
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('headless')
    if downloadPath is not None:
        prefs = {}
        os.makedirs(downloadPath, exist_ok=True)
        prefs["profile.default_content_settings.popups"]=0
        prefs["download.default_directory"]=downloadPath
        options.add_experimental_option("prefs", prefs)
        
    browser = webdriver.Chrome(chrome_options=options, executable_path=CHROMEDRIVER_PATH)
    return browser


filtered = list(filter(regex.match, fileList))
print(filtered)

driver = newChromeBrowser(downloadPath = os.getcwd())

for item in filtered:
    serachTerm = 'https://www.podnapisi.net/en/subtitles/search/?keywords=' + item
    driver.get(serachTerm)
    try:
        downloadBtn = driver.find_element_by_xpath('//*[@id="page-body"]/div[4]/div/div[6]/table/tbody/tr[1]/td[1]/div[1]/a[1]')
        downloadBtn.click()
    except:
        continue
    