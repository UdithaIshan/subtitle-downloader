import os

fileList = os.listdir()

def check(name):
    if 'py' in name:
        return True
    else:
        return False

filtered = filter(check, fileList)

for s in filtered:
    print(s)