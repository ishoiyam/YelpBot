from selenium import webdriver
import time

"""
search for terms and scrape data for each term, by scraping and crawling...
"""


class YelpBot(object):
    def __init__(self):
        self.url = "https://www.yelp.com/"
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        
    def close_session(self):
        print("[+] Clossing Session...")
        time.sleep(4)
        self.driver.close()

    def submit_button(self):
        btn = self.driver.find_element_by_xpath("//*[@id='header-search-submit']")
        btn.click()

    def input_fields(self, service="takeout", location="San Francisco, CA"):
        service_pl = self.driver.find_element_by_xpath("//*[@id='find_desc']")
        location_pl = self.driver.find_element_by_xpath("//*[@id='dropperText_Mast']")
        
        service_pl.clear()
        location_pl.clear()
        
        service_pl.send_keys(service)
        location_pl.send_keys(location)

    def extract_posts(self):
        results = self.driver.find_element_by_tag_name("ul")
        posts = results.find_elements_by_tag_name("li")
        for post in posts:
            print("\n********************")
            print(post.text)



if __name__ == "__main__":
    st_yelp = YelpBot()
    st_yelp.input_fields()
    st_yelp.submit_button()
    st_yelp.extract_posts()
    st_yelp.close_session()
