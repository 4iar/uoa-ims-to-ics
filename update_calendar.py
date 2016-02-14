from redis import Redis
from seminar_parser import fetch_events_as_ics
from datetime import datetime
from config_parser import Config

config = Config()


def update_calendar():
    redis_store = Redis(host=config.get('REDIS', 'Host'),
                        port=config.get('REDIS', 'Port'),
                        db=config.get('REDIS', 'Db'))
    redis_store.set('calendar', fetch_events_as_ics())
    redis_store.set('last_updated', datetime.now().toordinal())
