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

    def start_driver(self):
        self.driver = webdriver.Chrome()

    def redirect_tag_page(self, tag):
        url = f'https://twitter.com/i/flow/login?redirect_after_login=%2Fhashtag%2F{tag}%3Fsrc%3Dhashtag_click%26f%3Dlive'
        self.driver.get(url)

    def input_user_id(self, user_id):
        self.driver.implicitly_wait(6000)

        input_element = self.driver.find_element(By.CLASS_NAME, 'r-30o5oe')
        input_element.send_keys(user_id)
        input_element.send_keys(Keys.RETURN)

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
    
    def find_tweet_url(self, tweet):
        tweet_url_class = "css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-xoduu5 r-1q142lx r-1w6e6rj r-9aw3ui r-3s2u2q r-1loqt21"
        
        #/bang_dream_mygo/status/1759125601158606874
        tweet_url_element = tweet.find(attrs={'class': tweet_url_class})
        href_value = tweet_url_element.get('href')
        tweet_url = "https://twitter.com" + href_value

        return tweet_url
    
    def find_tweet_data(self, tweet):
        tweet_data_class = "css-175oi2r r-1kbdv8c r-18u37iz r-1wtj0ep r-1ye8kvj r-1s2bzr4"
        

    def remove_dupes_tweet(self, tweet_cells):
        
    
        for tweet_cell in tweet_cell:
            href_value = tweet_cell.find('a', {'href': True}).get('href')
    
    def find_tweets(self):
        tweets = []

        #시간지연 필수 안전빵으로 10초 박자
        time.sleep(10)
        self.driver.implicitly_wait(6000)
        html_source = self.driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')

        tweet_cell_inners = soup.find_all('div', {'data-testid': 'cellInnerDiv'})

        for te in tweet_cell_inners:
            self.find_tweet_url(te)
        #self.remove_dupes_tweet(tweet_cell_inners)
        
        # for tweet_cell_inner in tweet_cell_inners:
        #     tweet = tweet_cell_inner.find(attrs={'data-testid': 'tweet'})
        #     tweets.append(tweet)

        # return tweets
    
    def find_tweet_image(tweet):
        tweet_image = 1

    
