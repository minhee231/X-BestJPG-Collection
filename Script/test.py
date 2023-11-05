from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import time
import re 

global driver

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
    except: return

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

def inputPasswd(passwd):
    global driver

    driver.implicitly_wait(6000)
    
    
#예외처리 하세요
#1. 아이디 안물어보고 바로 passwd 넘어갈 때.
def Login(email,passwd,UserID):
    global driver

    inputEmail(email)

    #로그인 (비번 부분)
    input_element = driver.find_element(By.CLASS_NAME, 'r-30o5oe')
    try:
        input_element.send_keys(UserID)
        input_element.send_keys(Keys.RETURN)
        time.sleep(1)

        input_element = driver.find_element(By.CLASS_NAME, 'r-homxoj')
        input_element.send_keys(passwd)
        input_element.send_keys(Keys.RETURN)

    except:
        print("Login Error")

def maindesk(Tag,tweet_count):
    global driver
    TW_Count = 0
    tweet_dupSet = set()
    TweetData = {}

    driver.implicitly_wait(6000)
    while True:
        #트윗 검색
        tweets = driver.find_elements(By.XPATH, '//*[@data-testid="tweet"]')

        for tweet in tweets:
            if tweet not in tweet_dupSet:
                tweet_dupSet.add(tweet)
                Img_elements = tweet.find_elements(By.TAG_NAME, 'img')
                Aria_element = tweet.find_element(By.CSS_SELECTOR, '.css-1dbjc4n.r-1kbdv8c.r-18u37iz.r-1wtj0ep.r-1s2bzr4.r-1ye8kvj')
                Profile_info = tweet.find_element(By.CSS_SELECTOR, ".css-1dbjc4n.r-k4xj1c.r-18u37iz.r-1wtj0ep")
                pro = Profile_info.find_element(By.CSS_SELECTOR, ".css-1dbjc4n.r-1awozwy.r-18u37iz.r-1cmwbt1.r-1wtj0ep")

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
                        
        scrollPage()
        if TW_Count > tweet_count: break

    JsonFileName = f"./{Tag}.json"
    with open(JsonFileName, "w") as json_file:
        json.dump(TweetData, json_file)

#경로에 맞게 지정
Key_path = './key.json'
with open(Key_path, 'r', encoding="UTF-8") as KeyFile:
    KeyData = json.load(KeyFile)

Tags = KeyData["tags"]
email = KeyData["email"]
passwd = KeyData["passwd"]
UserID = KeyData["UserID"]
tweet_count = KeyData["tweet_count"]
KeyFile.close

#드라이버 셋팅
chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)
#chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
#chrome_options.add_argument('window-size=1920x1080')
#driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome(chrome_driver_path,options=chrome_options)
driver = webdriver.Chrome()

flag = 1
for Tag in Tags:
    url = f'https://twitter.com/hashtag/{Tag}?src=hashtag_click&f=live'
    driver.get(url)
    if flag:
        Login(email,passwd,UserID)
        flag = 0

    maindesk(Tag,tweet_count)



    
