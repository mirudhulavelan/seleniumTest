from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

user_name = driver.find_element_by_name('email')
user_name.send_keys('98429xxxx')

password = driver.find_element_by_name('pass')
password.send_keys('xxxxxx')

log_in_button = driver.find_element_by_id('u_0_b')
log_in_button.click()
time.sleep(5)

search_query = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[2]/div[2]/div/div/div/div/div[3]/label/input')

search_query.send_keys('python developers')

search_query.send_keys(Keys.RETURN)

