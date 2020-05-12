from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Chrome
driver = webdriver.Chrome(executable_path="/home/hadi/Documents/github/Tutorial/chromedriver")
url1 = "https://www.expedia.com/"
url2="https://testautomationpractice.blogspot.com/"
driver.get(url1)
print (driver.title) # return the title of the page
print (driver.current_url) # return URL of the page
#driver.find_element_by_xpath("//*[@id='wizard-hotel-pwa-v2-1']/div[2]/div/button").click()

driver.get(url2)
print (driver.title) # return the title of the page
print (driver.current_url) # return URL of the page
time.sleep(5)
driver.back()
print ("Back:" + driver.title) # return the title of the page
print ("Back:" + driver.current_url) # return URL of the page
time.sleep(5)
driver.forward()
print ("Forward:" + driver.title) # return the title of the page
print ("Forward:" + driver.current_url) # return URL of the page

time.sleep(5)
driver.close()