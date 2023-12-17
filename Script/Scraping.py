from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import boto3
import json
import time
import re

global driver
global s3

def setImageUrl(image_src):
    if 'media' in image_src:
        url_parts = image_src.split('&')

        for i, part in enumerate(url_parts):
            if part.startswith('name='):
                url_parts[i] = 'name=large'
        return '&'.join(url_parts)
    
    else: return

def setImageJson(image_elements):
    count = 0
    flag = False
    image_data = {"imgs" : {}}
    
    for image_element in image_elements:
        image_src = setImageUrl(image_element.get_attribute('src'))
        if image_src:
            image_data['imgs']["img"+str(count)] = image_src
            count += 1
            flag = True
        
    if flag: return image_data

def setAria(aria_element):
    try:
        aria_attribute = aria_element.get_attribute("aria-label")
        pattern = r'(\d+)\s+(\w+)'
        matches = re.findall(pattern, aria_attribute)
        return matches # (키, 벨류)
    except: return
    
def scrollPage():
    global driver

    time.sleep(0.2)
    driver.implicitly_wait(6000)
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.PAGE_DOWN)

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

def login(user_id,password):
    global driver

    try: 
        inputUserID(user_id)
        driver.implicitly_wait(6000)
        time.sleep(1)

        inputPassword(password)
        
    except:
        print("Login Error")

def createJsonFile(file_name,file_data):
    tweet_data_json = json.dumps(file_data)

    with open(f"./{file_name}", 'w') as file:
        file.write(tweet_data_json)

def uploadJson(file_name):
    global s3
    global bucket_name
    global dir_path

    s3.put_object(Body=open(f"./{file_name}", 'rb'), Bucket=bucket_name, Key=f"{dir_path}/{file_name}", ACL='public-read')

def findTweet(tag,search_limit):
    global driver
    global s3
    tweet_count = 0
    new_tweet = 0
    tweet_set = set()
    tweet_data = {}
    driver.implicitly_wait(6000)
    json_file_name = f"{tag}.json"

    while True:
        tweets = driver.find_elements(By.XPATH, '//*[@data-testid="tweet"]')
        for tweet in tweets:
            if tweet not in tweet_set: #중복제거
                tweet_set.add(tweet)
                try:
                    image_elements = tweet.find_elements(By.TAG_NAME, 'img')
                    aria_element = tweet.find_element(By.XPATH,'//*[@class="css-175oi2r r-1kbdv8c r-18u37iz r-1wtj0ep r-1ye8kvj r-1s2bzr4"]')
                    profile_information = tweet.find_element(By.XPATH,'//*[@class="css-175oi2r r-k4xj1c r-18u37iz r-1wtj0ep"]')
                    ad_element = profile_information.find_element(By.XPATH,'//*[@class="css-1qaijid r-bcqeeo r-qvutc0 r-poiln3"]')                    
                except:
                    print("element found error")

                try:
                    if ad_element.text != 'Ad':
                        imgage_datas = setImageJson(image_elements)
                        aria_datas = setAria(aria_element)

                        if aria_datas and imgage_datas:
                            tweet_number = "Tweet" + str(tweet_count)
                            tweet_data[tweet_number] = {}
                            
                            #json에 aria data 추가
                            for aria_data in aria_datas:
                                value, key = aria_data
                                tweet_data[tweet_number][key.lower()] = int(value)

                            #json에 imgs 추가
                            tweet_data[tweet_number]["imgs"] = imgage_datas.get("imgs")                          
                            tweet_count += 1
                            new_tweet = 0
                            createJsonFile(json_file_name,tweet_data)
                except: print("save data error")
        scrollPage()

        new_tweet += 1
        if new_tweet > 20:
            uploadJson(json_file_name)
            print("API 요청 수 초과")
            print(f"{tag}, 집계된 트윗 수: {tweet_count}",)
            return
        if tweet_count > search_limit:
            uploadJson(json_file_name)
            print(f"{tag}, 집계된 트윗 수: {tweet_count}",)
            return

#함수 ========================================================
        
key_path = './key.json'
key_path = 'C:/Users/goomi/Downloads/key.json'
with open(key_path, 'r', encoding="UTF-8") as keyFile:
    key_data = json.load(keyFile)

tags = key_data["TWITTER"]["tags"]
password = key_data["TWITTER"]["password"]
user_id = key_data["TWITTER"]["user_id"]
search_limit = key_data["TWITTER"]["search_limit"]

aws_access_key_id = key_data["AWS"]["aws_access_key_id"]
aws_secret_access_key = key_data["AWS"]["aws_secret_access_key"]
region_name = key_data["AWS"]["region_name"]
bucket_name = key_data["AWS"]["bucket_name"]
dir_path = key_data["AWS"]["bucket_dir_name"]

s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
driver = webdriver.Chrome()

count = 0
for tag in tags:
    url = f'https://twitter.com/i/flow/login?redirect_after_login=%2Fhashtag%2F{tag}%3Fsrc%3Dhashtag_click%26f%3Dlive'
    driver.get(url)
    driver.implicitly_wait(6000)
    login(user_id[count],password)
    findTweet(tag,search_limit)
    count += 1
    #드라이버 초기화
    driver.delete_all_cookies()


    
