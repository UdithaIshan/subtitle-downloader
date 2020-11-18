from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import re

fileList = os.listdir("E:\Mandalorian")
regex = re.compile(".*\.(mp4|avi|flv|mkv|mov|wmv)$")

filtered = list(filter(regex.match, fileList))
print(filtered)

serachTerm = 'https://www.podnapisi.net/en/subtitles/search/?keywords=' + filtered[0]
print(serachTerm)

driver = webdriver.Chrome()
driver.get(serachTerm)
downloadBtn = driver.find_element_by_xpath('//*[@id="page-body"]/div[4]/div/div[6]/table/tbody/tr[1]/td[1]/div[1]/a[1]')
downloadBtn.click()
# searchBox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
# searchBox.send_keys(serachTerm + Keys.ENTER)