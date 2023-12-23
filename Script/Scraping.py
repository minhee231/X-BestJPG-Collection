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
        if image_elements and image_element:
            try:
                image_src = setImageUrl(image_element.get_attribute('src'))
            except: return
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
    
def scrollDownPage():
    global driver

    time.sleep(0.3)
    driver.implicitly_wait(6000)
    # current_scroll_position = driver.execute_script("return window.scrollY;")
    # new_scroll_position = current_scroll_position + 300
    # driver.execute_script(f"window.scrollTo(0, {new_scroll_position});")
    
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.PAGE_DOWN)
    driver.implicitly_wait(6000)

def scrollUpPage():
    current_scroll_position = driver.execute_script("return window.scrollY;")
    new_scroll_position = max(0, current_scroll_position - 300)
    driver.execute_script(f"window.scrollTo(0, {new_scroll_position});")

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

def uploadJson(file_name,dir_path):
    global s3tr
    global bucket_name

    s3.put_object(Body=open(f"./{file_name}", 'rb'), Bucket=bucket_name, Key=f"{dir_path}/{file_name}", ACL='public-read')

def findTweet(tag,search_limit,dir_path):
    global driver
    global s3

    tweet_count = 0
    new_tweet = 0
    tweet_set = set()
    aria_set = set()
    tweet_data = {}
    json_file_name = f"{tag}.json"

    while True:
        driver.implicitly_wait(6000)
        tweets = driver.find_elements(By.XPATH, '//*[@data-testid="cellInnerDiv"]')
        for tweet in tweets:
            if tweet not in tweet_set: #중복제거
                tweet_set.add(tweet)                
                try:
                    tw = tweet.find_element(By.XPATH, '//*[@data-testid="tweet"]')
                    image_elements = tw.find_elements(By.TAG_NAME, 'img')
                    aria_element = tw.find_element(By.XPATH,'//*[@class="css-175oi2r r-1kbdv8c r-18u37iz r-1wtj0ep r-1ye8kvj r-1s2bzr4"]')
                except: print("element error")
                #     profile_information = tw.find_element(By.XPATH,'//*[@class="css-175oi2r r-k4xj1c r-18u37iz r-1wtj0ep"]')
                #     ad_element = profile_information.find_element(By.XPATH,'//*[@class="css-1qaijid r-bcqeeo r-qvutc0 r-poiln3"]')                    
                # except:
                #     pass
                # for image_element in image_elements:
                #     print(image_element.get_attribute('src'))

                #전에 있는 요소를 불러와서 에러가 발생 img_element 초기화 설정해주면 될듯
                #if ad_element.text != 'Ad':
                imgage_datas = setImageJson(image_elements)
                aria_datas = setAria(aria_element)
            

                if aria_datas and imgage_datas:
                    tweet_number = "Tweet" + str(tweet_count)
                    tweet_data[tweet_number] = {}
                    
                    aria_tuple = tuple(sorted(aria_datas)) 
                    if aria_tuple not in aria_set:
                        aria_set.add(aria_tuple)
                        for aria_data in aria_datas:
                            value, key = aria_data
                            tweet_data[tweet_number][key.lower()] = int(value)

                        #json에 imgs 추가
                        tweet_data[tweet_number]["imgs"] = imgage_datas.get("imgs")                          
                        tweet_count += 1
                        new_tweet = 0
                        createJsonFile(json_file_name,tweet_data)

            
        scrollDownPage()
                                                                                                                                                                                                                                                                                                                                                                                                                            
        new_tweet += 1
        if new_tweet > 30:
            uploadJson(json_file_name, dir_path)
            print("API 요청 수 초과")
            print(f"{tag}, 집계된 트윗 수: {tweet_count}",)
            return
        
        if tweet_count > search_limit:
            uploadJson(json_file_name, dir_path)
            print(f"{tag}, 집계된 트윗 수: {tweet_count}",)
            return
        
def changeTweetNumber(start_number,best_json):
    chang_json = {}

    try:
        with open(f'./{best_json}', 'r', encoding="UTF-8") as keyFile:
            tweet_json = json.load(keyFile)

        for tweet_info in tweet_json.values():
            chang_json[f'Tweet{start_number}'] = tweet_info
            
        return chang_json
    except: return {}

def removeDuplicates(existing_json,new_data):
    try:
        with open(f'./{existing_json}', 'r', encoding="UTF-8") as keyFile:
            existing_datas = json.load(keyFile) #best json
    except:
        existing_datas = dict()
    if new_data not in existing_datas.values():
        return True
        
    else: return


        
def splitBestTweet(json_file, dir_path):
    likes = 0
    tweet_counts = [
    {'count': 0, 'data': {}, 'filename': f'best100_{json_file}', 'min_likes': 100},
    {'count': 0, 'data': {}, 'filename': f'best300_{json_file}', 'min_likes': 300},
    {'count': 0, 'data': {}, 'filename': f'best500_{json_file}', 'min_likes': 500},
    {'count': 0, 'data': {}, 'filename': f'best1000_{json_file}', 'min_likes': 1000},
    {'count': 0, 'data': {}, 'filename': f'best3000_{json_file}', 'min_likes': 3000}
    ]

    with open(f'./{json_file}', 'r', encoding="UTF-8") as keyFile:
        tweet_json = json.load(keyFile) #latest json

    for tweet_info in tweet_json.values():
        if 'likes' in tweet_info:
            likes = tweet_info["likes"]

            for tweet_count in tweet_counts:
                if likes >= tweet_count['min_likes']:
                    if removeDuplicates(tweet_count['filename'],tweet_info):
                        tweet_count['data'][f'Tweet{tweet_count["count"]}'] = tweet_info
                        tweet_count['count'] += 1
            
    for tweet_count in tweet_counts:
        tweet_count['data'].update(changeTweetNumber(tweet_count['count'], tweet_count['filename']))
        with open(f'./{tweet_count["filename"]}', 'w') as file:
            file.write(json.dumps(tweet_count['data']))

        uploadJson(tweet_count['filename'], dir_path)


#함수 ========================================================
        
key_path = './key.json'
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
latest_dir_path = key_data["AWS"]["latest_dir_path"]
best_dir_path = key_data["AWS"]["best_dir_path"]

s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
driver = webdriver.Chrome()

count = 0
for tag in tags:
    url = f'https://twitter.com/i/flow/login?redirect_after_login=%2Fhashtag%2F{tag}%3Fsrc%3Dhashtag_click%26f%3Dlive'
    driver.get(url)
    driver.implicitly_wait(6000)
    login(user_id[count],password)
    findTweet(tag,search_limit, latest_dir_path)
    count += 1
    #드라이버 초기화
    driver.delete_all_cookies()
    splitBestTweet(f'{tag}.json', best_dir_path)