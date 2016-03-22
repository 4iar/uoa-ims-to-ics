import subprocess
from .update_calendar import update_calendar
import time
from .config_parser import Config

if __name__ == '__main__':

    config = Config()

    subprocess.Popen(['python3', './ims_to_ics/app.py'])

    while True:
        update_calendar()
        time.sleep(60*config.getint('DEFAULT',
                                    'CalendarUpdateIntervalMinutes'))
