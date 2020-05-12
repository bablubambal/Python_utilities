#Whats up automatiion
#Sending the unlimited number of messages to the speicfic user
#using Selenium to automate
from selenium import webdriver 
from time import sleep
#Select the web Driver and Download it for any Browser u want to use
#Give the full path to the Driver
driver = webdriver.Chrome('/Users/Mohit Kumar/chromedriver')
#User Gets the Website
driver.get("https://web.whatsapp.com/");


input("Enter anything after qr code is scanned")
name = input("Enter the name :  ")
msg = input("enter the message : ")
count = int(input("enter the count: "))
time  = int(input("enter time in seconds "))



user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_1Plpp')
#we repeat the same msg till the count
for i in range(count):
	msg_box.send_keys(msg)
	sleep(time)
	button = driver.find_element_by_class_name('_35EW6')
	button.click()
