import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest


driver = webdriver.Chrome()
#driver.get("http://millionaire-academy.local/")
#element = driver.find_element(By.LINK_TEXT,"Login")
# driver.get("https://google.co.in/search?q=geeksforgeeks")
# driver.implicitly_wait(50000)
driver.get("https://www.google.com/")
element = driver.find_element(By.ID, "APjFqb")
element.send_keys("Python selenium mastering")
driver.maximize_window()
action = ActionChains(driver)
action.key_down(Keys.ENTER).key_up(Keys.CONTROL).perform()
#action.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()
time.sleep(20)
# driver.close()
# by_x_path = driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/textarea[1]")
# print (by_x_path)
# order to search element by Element => id -> name -> class name -> tag name -> link text / partial link text -> css selector -> xPath