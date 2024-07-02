from selenium import webdriver
from selenium.webdriver.edge.options import Options 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 

options = Options()
options.add_experimental_option("detach",True) 

browser = webdriver.Edge(options=options)
browser.maximize_window() 

url = "https://"
browser.get(url) 

browser.title 
button2 = browser.find_elements(By.CLASS_NAME, "button2")
user_input = browser.find_elements(By.ID, "TEST") 
user_input.send_keys("TEST") 
button2.click()

consent = browser.find_element(By.XPATH, '//button[2]/p').click()
content = browser.find_element(By.XPATH, '//*[@id="cat5"]/select')
content.click()
content.send_keys("TEST", Keys.ENTER)
search = browser.find_element(By.XPATH, '//*[@id="button2"]').click()
