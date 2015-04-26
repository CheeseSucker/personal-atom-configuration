import os

# Install packages in list
with open('packagelist.txt') as file:
    for package in file.readlines():
        os.system("apm install " + package)
