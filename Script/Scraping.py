from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import boto3
import json
import time
import re 

global driver
global s3
global bucket_name
global dir_path

def urlSet(url):
    url_parts = url.split('&')

    for i, part in enumerate(url_parts):
        if part.startswith('name='):
            url_parts[i] = 'name=large'
    return '&'.join(url_parts)
    
def setImgUrl(imgsrc):
    if 'media' in imgsrc:
        return urlSet(imgsrc)
    else: return

#aria-label의 키&벨류 
def setAria(aria_data):
    try:
        aria_attribute = aria_data.get_attribute("aria-label")
        pattern = r'(\d+)\s+(\w+)'
        matches = re.findall(pattern, aria_attribute)
        return matches # (키, 벨류)
    except: 
        return

def setImg(imgs):
    count = 0
    flag = 0
    img_data = {"imgs" : {}}
    try:
        for img in imgs:
            Img_src = setImgUrl(img.get_attribute('src'))
            if Img_src:
                flag = 1
                img_data["imgs"]["img" + str(count)] = setImgUrl(Img_src)
                count += 1
            
        if flag: return img_data
    except: return

def scrollPage():
    global driver
    time.sleep(0.2)
    driver.implicitly_wait(6000)
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.PAGE_DOWN)

def inputEmail(email):
    global driver
    driver.implicitly_wait(6000)

    input_element = driver.find_element(By.CLASS_NAME, 'r-30o5oe')
    input_element.send_keys(email)
    input_element.send_keys(Keys.RETURN)

def inputPassword(password):
    global driver
    driver.implicitly_wait(6000)

    input_element = driver.find_element(By.CLASS_NAME, 'r-homxoj')
    input_element.send_keys(password)
    input_element.send_keys(Keys.RETURN)

    
def inputUserID(UserID):
    global driver
    driver.implicitly_wait(6000)

    input_element = driver.find_element(By.CLASS_NAME, 'r-30o5oe')
    input_element.send_keys(UserID)
    input_element.send_keys(Keys.RETURN)

def Login(email,password,UserID):
    global driver

    try:                                                                                                             
        inputEmail(email)

        input_element = driver.find_element(By.CLASS_NAME, 'r-homxoj')
        element_type = input_element.get_attribute("type")

        if 'text' in element_type:
            inputUserID(UserID)
        
        inputPassword(password)
    except:
        print("Login Error")

def Logout():
    global driver
    driver.implicitly_wait(6000)

    element = driver.find_element(By.XPATH, '//*[@aria-label="Account menu"]')
    time.sleep(0.5)
    element.send_keys(Keys.ENTER)

    element = driver.find_element(By.XPATH, '//*[@data-testid="AccountSwitcher_Logout_Button"]')
    driver.implicitly_wait(6000)
    element.click()

    element = driver.find_element(By.XPATH, '//*[@data-testid="confirmationSheetConfirm"]')
    driver.implicitly_wait(6000)
    time.sleep(0.5)
    element.send_keys(Keys.ENTER)

def CreateJsonFile(FileName,FileData):
    TweetDataJSON = json.dumps(FileData)

    with open(f"./{FileName}", 'w') as file:
        file.write(TweetDataJSON)

def UploadJson(FileName):
    global s3
    global bucket_name
    global dir_path

    s3.put_object(Body=open(f"./{FileName}", 'rb'), Bucket=bucket_name, Key=f"{dir_path}/{FileName}", ACL='public-read')

def maindesk(Tag,tweet_count):
    global driver
    global s3
    TW_Count = 0
    NewTweet = 0
    tweet_dupSet = set()
    TweetData = {}
    driver.implicitly_wait(6000)
    jsonfile = f"{Tag}.json"
    while True:
        #트윗 검색
        tweets = driver.find_elements(By.XPATH, '//*[@data-testid="tweet"]')

        for tweet in tweets:
            if tweet not in tweet_dupSet:
                tweet_dupSet.add(tweet)
                try:
                    Img_elements = tweet.find_elements(By.TAG_NAME, 'img')
                    Aria_element = tweet.find_element(By.CSS_SELECTOR, '.css-1dbjc4n.r-1kbdv8c.r-18u37iz.r-1wtj0ep.r-1s2bzr4.r-1ye8kvj')
                    Profile_info = tweet.find_element(By.CSS_SELECTOR, ".css-1dbjc4n.r-k4xj1c.r-18u37iz.r-1wtj0ep")
                    pro = Profile_info.find_element(By.CSS_SELECTOR, ".css-1dbjc4n.r-1awozwy.r-18u37iz.r-1cmwbt1.r-1wtj0ep")
                except:
                    print("element find error")

                try:
                    if pro.text != 'Ad':
                        aria_datas = setAria(Aria_element)
                        img_datas = setImg(Img_elements)

                        if aria_datas and img_datas:
                            tweet_number = "Tweet" + str(TW_Count)
                            TweetData[tweet_number] = {}
                            
                            #json에 aria data 추가
                            for aria_data in aria_datas:
                                value, key = aria_data
                                TweetData[tweet_number][key.lower()] = int(value)

                            #json에 imgs 추가
                            TweetData[tweet_number]["imgs"] = img_datas.get("imgs")
                            TW_Count += 1 #AD false
                            NewTweet = 0
                            CreateJsonFile(jsonfile,TweetData)
                except: print("save data error")
        scrollPage()
        NewTweet += 1
        if NewTweet > 20:
            UploadJson(jsonfile)
            print("API 요청 수 초과")
            print(f"{Tag}, 집계된 트윗 수: {TW_Count}",)
            return
        if TW_Count > tweet_count:
            UploadJson(jsonfile)
            print(f"{Tag}, 집계된 트윗 수: {TW_Count}",)
            return

Key_path = './key.json'
Key_path = 'C:/Users/goomi/OneDrive/바탕 화면/작업/Desk/X-BestJPG-Collection/Script/key.json'
with open(Key_path, 'r', encoding="UTF-8") as KeyFile:
    KeyData = json.load(KeyFile)

Tags = KeyData["Twitter"]["tags"]
emails = KeyData["Twitter"]["Accounts"]["Emails"]
passwords = KeyData["Twitter"]["Accounts"]["Passwords"]
UserIDs = KeyData["Twitter"]["Accounts"]["UserIDs"]
SamePasswd = KeyData["Twitter"]["Accounts"]["PasswordSame"]
tweet_count = KeyData["Twitter"]["tweet_count"]
aws_access_key_id = KeyData["AWS"]["aws_access_key_id"]
aws_secret_access_key = KeyData["AWS"]["aws_secret_access_key"]
region_name = KeyData["AWS"]["region_name"]
bucket_name = KeyData["AWS"]["bucket_name"]
dir_path = KeyData["AWS"]["bucket_dir_name"]

s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#드라이버 셋팅
chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)
#chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
#chrome_options.add_argument('window-size=1920x1080') 
#driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome(chrome_driver_path,options=chrome_options)
driver = webdriver.Chrome()


NextCount = 0
for Tag in Tags:
    driver.implicitly_wait(6000)
    driver.refresh()
    url = f'https://twitter.com/i/flow/login?redirect_after_login=%2Fhashtag%2F{Tag}%3Fsrc%3Dhashtag_click%26f%3Dlive'
    driver.get(url)
    driver.refresh()

    if SamePasswd:
        Login(emails[NextCount],passwords[0],UserIDs[NextCount])

    else:
        Login(emails[NextCount],passwords[NextCount],UserIDs[NextCount])
    NextCount += 1

    maindesk(Tag,tweet_count)
    Logout()