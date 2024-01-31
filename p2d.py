from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(2)

username = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
username.send_keys("Admin")
time.sleep(2)

password = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
password.send_keys("admin123")
time.sleep(5)
login=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

login.click()
time.sleep(10)


mainmenu_items=driver.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li')
expated_items=["Admin","PIM","Leave","Time","Recruitment","My Info","Performance","Dashboard","Directory","Maintenance","Claim","Buzz"]
for items in mainmenu_items:
    if items.text in expated_items:
        print ("all ierms persent")
        
    else: 
        print("no item prasents")

# for items in mainmenu_items:    
#     print(items.text)
        
       
    

time.sleep(5)
driver.quit()