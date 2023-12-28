from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

driver = webdriver.Chrome()

path = "C:/Users/goomi/Downloads/best3000_mygo.json"
with open(f"{path}","r") as file:
    tweets = json.load(file)

for tweet in tweets.values():
    for i in tweet['imgs'].values():
        driver.get(i)
        time.sleep(1)