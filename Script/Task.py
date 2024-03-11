from Scraping_Module import TwitterHandler
import sys
import time, json

key_path = './config/key.json'
with open(key_path, 'r', encoding="UTF-8") as keyFile:
    key_data = json.load(keyFile)


#config
tag = sys.argv[1]
user_id = sys.argv[2]
password = sys.argv[3]
search_limit = key_data["twitter"]["search_limit"]
print(search_limit)


twitter_handler = TwitterHandler()

twitter_handler.start_driver()
twitter_handler.redirect_tag_page(tag)
twitter_handler.login(user_id, password)
time.sleep(10)
twitter_handler.run_tweet_task(search_limit)



time.sleep(1000)