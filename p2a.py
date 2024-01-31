from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
time.sleep(5)

username = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
username.send_keys("anbu")
time.sleep(5)

password = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
password.send_keys("anbu123")
time.sleep(5)
login=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

login.click()
time.sleep(5)

resetpassword=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')

resetpassword.click()
time.sleep(5)


username = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input')
username.send_keys("Admin")
time.sleep(5)

resetpassword=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')

resetpassword.click()
time.sleep(5)


driver.quit()

