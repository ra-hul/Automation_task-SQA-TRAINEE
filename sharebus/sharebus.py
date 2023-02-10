from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj=Service("C:\Drivers\Chrome\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://test.sharebus.co/")
# driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH, "//*[@id='app']/nav/div/ul/li/button").click()
driver.find_element(By.ID, "email").send_keys("brainstation23@yopmail.com")
driver.find_element(By.ID, "password").send_keys("Pass@1234")

driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div/form/div[4]/button").click()

time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div/div/div").click()
driver.find_element(By.XPATH,"//li[@aria-label='sharelead']//span[contains(text(),'Sharelead')]").click()


driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div/div/button/span[1]").click() #continue button
# time.sleep(5)

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/button").click()
driver.find_element(By.ID,"startPoint").send_keys("Oslo,Norway")
driver.find_element(By.ID, "destination").send_keys("Kolbotn, Norway")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/div[2]/div[1]/div/form/div[1]/div[3]/div[1]/div[1]/div/div[1]/span/input").send_keys("22.02.2023")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/div[2]/div[1]/div/form/div[1]/div[3]/div[1]/div[1]/div/div[2]/span/input").send_keys("14:30")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/div[2]/div[1]/div/form/div[1]/div[3]/div[2]/div[1]/div/div[1]/span/input").send_keys("26.02.2023")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/div[2]/div[1]/div/form/div[1]/div[3]/div[2]/div[1]/div/div[2]/span/input").send_keys("15:00")

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/div[2]/div[1]/div/form/div[2]/button[2]").click()
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[1]/button[1]").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/i").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/ul/li[4]").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/div[2]/div[1]/div/div[2]/button[2]").click()

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/button[2]").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/button[2]").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[4]/button[2]").click()

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[4]/button").click()

driver.find_element(By.XPATH,"//*[@id='app']/nav/div/ul/li[1]/button").click()
