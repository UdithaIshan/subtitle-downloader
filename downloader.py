from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import re

fileList = os.listdir()
regex = re.compile(".*\.(mp4|avi|flv|mkv|mov|wmv)$")

filtered = filter(regex.match, fileList)

driver = webdriver.Chrome()
driver.get('https://google.com')
searchBox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchBox.send_keys('Uditha Ishan' + Keys.ENTER)