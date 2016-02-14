import subprocess
from update_calendar import update_calendar
import time

if __name__ == '__main__':

    subprocess.Popen(['./app.py'])

    while True:
        calendar_update_interval_minutes = 30
        update_calendar()
        time.sleep(60*calendar_update_interval_minutes)
