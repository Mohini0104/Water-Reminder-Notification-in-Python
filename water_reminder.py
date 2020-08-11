import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please, Drink Water",
            message ="Bhai pani peile,skin ki quality dekhi h teri, chii lolll",

            timeout =5
        )
        time.sleep(60*60)