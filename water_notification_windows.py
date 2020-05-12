#Water Drinkin Notification System
import time
from plyer import notification
#plyer module notification is used to display the notifiction
while True:

    if __name__ == "__main__":
        notification.notify(
            title = "Drink Water",
            #Any message to be displayed
            message = "Drink more and more water and  you will be healthy;",
            #Give the full path of the icon to be displayed in app_icon
            app_icon =  "C:/Users/Mohit Kumar/Desktop/water notication/icon.ico",
            timeout  = 3
        )
        time.sleep(60*60)
