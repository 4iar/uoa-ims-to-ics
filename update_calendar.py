from ims_to_ics.seminar_parser import fetch_events_as_ics
from ims_to_ics.config_parser import Config
from ims_to_ics.database import Database

config = Config()


def update_calendar():
    db = Database()
    db.insert_ics(fetch_events_as_ics())
    db.commit()
    db.close()

if __name__ == '__main__':
    update_calendar()
