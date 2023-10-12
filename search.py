from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

driver = webdriver.Edge(executable_path='C:\')

driver.get("https://www.google.com")

search_queries = ["cats", "dogs", "flowers", "mountains", "beaches"]

num_searches = 17

for _ in range(num_searches):
    search_query = random.choice(search_queries)
    
    search_input = driver.find_element_by_name("q")
    search_input.clear()
    search_input.send_keys(search_query)
    
    search_input.send_keys(Keys.RETURN)
    
    time.sleep(3)

driver.quit()
