from selenium import webdriver 
from time import sleep
driver = webdriver.Chrome('/Users/Mohit Kumar/chromedriver') 
driver.get("https://web.whatsapp.com/");

input("Enter anything after qr code is scanned ")

def fun():
    name = input("Enter the name:")
    msg = input("enter the message : ")
    count = int(input("enter the count: "))
    time  = int(input("enter time in seconds "))
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_class_name('_1Plpp')
    for i in range(count):
        msg_box.send_keys(msg)
        sleep(time)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()
while(1):
    print("Enter 1 to perform function and to 2 exit") 
    choice = int(input("Enter your choice"))
    if(choice == 1):
        print("exectuing the function")
        fun()
    else:
        print("Exiting the loop ")
        break

print("Script Execution Success")
    

    








