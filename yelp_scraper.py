from selenium import webdriver
import time

class YelpBot(object):
    def __init__(self):
        self.url = "https://www.yelp.com/"
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
    
    def close_session(self):
        print("[+] Clossing Session...")
        time.sleep(4)
        self.driver.close()


if __name__ == "__main__":
    st_yelp = YelpBot()
    st_yelp.close_session()
