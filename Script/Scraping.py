from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import boto3
import json
import time
import re

global driver
global key_data

def fetchKeyJson():
    global key_data
    key_path = './key.json'

    with open(key_path, 'r', encoding="UTF-8") as key_file:
        key_data = json.load(key_file)

def startDriver():
    global driver
    driver = webdriver.Chrome()

def redirectTagPage(tag):
    global driver
    url = f'https://twitter.com/i/flow/login?redirect_after_login=%2Fhashtag%2F{tag}%3Fsrc%3Dhashtag_click%26f%3Dlive'
    driver.get(url)

def inputUserID(user_id):
    global driver
    driver.implicitly_wait(6000)

    input_element = driver.find_element(By.CLASS_NAME, 'r-30o5oe')
    input_element.send_keys(user_id)
    input_element.send_keys(Keys.RETURN)

def inputPassword(password):
    global driver
    driver.implicitly_wait(6000)

    input_element = driver.find_element(By.CLASS_NAME, 'r-homxoj')
    input_element.send_keys(password)
    input_element.send_keys(Keys.RETURN)

def login(user_id, password):
    try:
        inputPassword(user_id)
        time.sleep(1)
        inputPassword(password)

    except:
        print("Login Error")

def startScraping():
    key_json = fetchKeyJson()
    


#====test
fetchKeyJson()
startDriver()
redirectTagPage(key_data["TWITTER"]["tags"][0])
login("pjsekainull0","brainpower123")

time.sleep(1000)