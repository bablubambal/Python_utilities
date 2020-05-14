
from selenium import webdriver 
from time import sleep
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.keys import Keys

#Select the web Driver and Download it for any Browser u want to use
#Give the full path to the Driver
driver = webdriver.Chrome('/Users/Mohit Kumar/chromedriver')
#User Gets the Website
driver.get("https://www.instagram.com/")


# input(username and password for your account)
username = "<username>"
password = "<password>"
sleep(10)
username_input = driver.find_element_by_css_selector("input[name='username']")
password_input = driver.find_element_by_css_selector("input[name='password']")
username_input.send_keys(username)
password_input.send_keys(password)
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
sleep(12)
sleep(2)
dialogue = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
dialogue.click()
sleep(5)
first_user = driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
first_user.click()
sleep(4)
msgsperson = driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div")
msgsperson.click()
sleep(5)
msgbox = driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
#person = driver.find_element_by_xpath("//*[@id='f3bcf589ea6d8e']/div/div/div/div")
for i in range(10):
    msgbox.send_keys("You are hacked",i)
    character = driver.find_element_by_xpath()
    msgbox.send_keys(Keys.ENTER)
driver.quit()


