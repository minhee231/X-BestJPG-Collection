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

class TwitterHandler:
    def __init__(self):
        self.driver = None
        self.key_data = None
        self.tweets_set = set()
        self.succes_icon = '\u2713'
        self.error_icon = '\u2717'
        self.

    def start_driver(self):
        try:
            self.driver = webdriver.Chrome()
            print(f"{self.succes_icon}Driver Start Success")
        except: print(f"{self.error_icon}Driver Start Error")

    def redirect_tag_page(self, tag):
        try:
            url = f'https://twitter.com/i/flow/login?redirect_after_login=%2Fhashtag%2F{tag}%3Fsrc%3Dhashtag_click%26f%3Dlive'
            self.driver.get(url)
            print("Page Redirction Success")

        except: print("Page Redirction Error")
        

    def input_user_id(self, user_id):
        try:
            self.driver.implicitly_wait(6000)

            input_element = self.driver.find_element(By.CLASS_NAME, 'r-30o5oe')
            input_element.send_keys(user_id)
            input_element.send_keys(Keys.RETURN)
        
        except: print("Input UserID Error")

    def down_scroll(self):
        time.sleep(0.3)
        self.driver.implicitly_wait(6000)

        body_element = self.driver.find_element(By.TAG_NAME, 'body')
        body_element.send_keys(Keys.PAGE_DOWN)
    def input_password(self, password):
        self.driver.implicitly_wait(6000)

        input_element = self.driver.find_element(By.CLASS_NAME, 'r-homxoj')
        input_element.send_keys(password)
        input_element.send_keys(Keys.RETURN)

    def login(self, user_id, password):
        try:
            self.input_user_id(user_id)
            time.sleep(1)
            self.input_password(password)
            self.driver.implicitly_wait(6000)

        except:
            #대충 로그에 넣기
            print("Login Error")
    
    def page_down(self):
        self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
        self.driver.implicitly_wait(6000)

    def find_tweet_url(self, tweet):
        tweet_url_class = "css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-xoduu5 r-1q142lx r-1w6e6rj r-9aw3ui r-3s2u2q r-1loqt21"
        
        #/bang_dream_mygo/status/1759125601158606874
        tweet_url_element = tweet.find(attrs={'class': tweet_url_class})
        if tweet_url_element:
            href_value = tweet_url_element.get('href')
            tweet_url = "https://twitter.com" + href_value
            return tweet_url

        else: return
    
    def process_tweet_data(self, tweet_data):
        pattern = r'(\d+)\s+(\w+)'
        matches = re.findall(pattern, tweet_data)
        return matches # (키, 벨류)

    
    def find_tweet_aria_data(self, tweet): #aria data
        tweet_data_class = "css-175oi2r r-1kbdv8c r-18u37iz r-1wtj0ep r-1ye8kvj r-1s2bzr4"

        tweet_data_element = tweet.find(attrs={'class': tweet_data_class})
        tweet_data_velue = tweet_data_element.get('aria-label')
        tweet_data_velue = self.process_tweet_data(tweet_data_velue)

        return tweet_data_velue
    
    def convert_image_to_json(self, image_urls): #url type is list
        image_count = 0
        image_json = {"imgs": {}}
        
        for image_url in image_urls:
            image_json['imgs']["img"+str(image_count)] = image_url
            image_count += 1

        return image_json

    # def convert_aria_data_to_json(self, aria_data): #aria_data type is tuple
    #     aria_data_json = 1 여기여기 깃허브 염탐하기

    def process_image_data(self, url):
        if 'media' in url:
            url_parts = url.split('&')

            for i, part in enumerate(url_parts):
                if part.startswith('name='):
                    url_parts[i] = 'name=large'
            return '&'.join(url_parts)
    
    def find_tweet_image_data(self, tweet): #aria data
        image_element_class = "css-9pa8cd"
        image_list = []

        tweet_image_elements = tweet.find_all(attrs={'class': image_element_class})
        for tweet_image_element in tweet_image_elements:
            tweet_image_velue = tweet_image_element.get('src')
            tweet_image_velue = self.process_image_data(tweet_image_velue)
            
            if tweet_image_velue:
                image_list.append(tweet_image_velue)

        return image_list
    
    def remove_dupes_tweet(self, tweet_cells):
        for tweet_cell in tweet_cells:
            tweet_url = self.find_tweet_url(tweet_cell)

            if tweet_url not in self.tweets_set:
                self.tweets_set.add(tweet_url)
                return True
            
            else: return
    
    def find_tweet_elements(self):
        tweets = []

        #시간지연 필수 안전빵으로 10초 박자
        #time.sleep(10)
        self.driver.implicitly_wait(6000)
        html_source = self.driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')

        tweet_cell_inners = soup.find_all('div', {'data-testid': 'cellInnerDiv'})
        
        return tweet_cell_inners

    def run_tweet_task(self, limit):
        for _limit in range(limit):
            tweet_cells = self.find_tweet_elements()

            for tweet_cell in tweet_cells:
                if self.remove_dupes_tweet(tweet_cell):
                    tweet_aria_datas = self.find_tweet_aria_data(tweet_cell)
                    tweet_image_datas = self.find_tweet_image_data(tweet_cell)
                    print(tweet_image_datas)
                
            self.page_down()
            #time.sleep(0.2)
            





    
