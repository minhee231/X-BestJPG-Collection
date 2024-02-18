from Scraping_Module import TwitterHandler
import sys
import time

#config
tag = sys.argv[1]
user_id = sys.argv[2]
password = sys.argv[3]

twitter_handler = TwitterHandler()

twitter_handler.start_driver()
twitter_handler.redirect_tag_page(tag)
twitter_handler.login(user_id, password)
twitter_handler.find_tweets()


time.sleep(1000)