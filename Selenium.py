from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Chrome
driver = webdriver.Chrome(executable_path="/home/hadi/Documents/github/Tutorial/chromedriver")

#driver.get("https://testautomationpractice.blogspot.com/")
driver.get("https://www.youtube.com/")
print (driver.title) # return the title of the page
print (driver.current_url) # return URL of the page


time.sleep(5)
driver.close()