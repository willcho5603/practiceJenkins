import os
import schedule
import datetime
from time import sleep
import task

def run_scripts():
    os.system("helloworld.py")
    os.system("name.py")


def main():
    schedule.every().day.at("00:00").do(run_scripts)
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
