import os
import re

fileList = os.listdir()
regex = re.compile(".*\.(mp4|avi|flv|mkv|mov|wmv)$")

filtered = filter(regex.match, fileList)
