import redis
from seminar_parser import fetch_events_as_ics
from datetime import datetime


def update_calendar():

    redis_store = redis.Redis(host='localhost', port=6379, db=0)
    redis_store.set('calendar', fetch_events_as_ics())
    redis_store.set('last_updated', datetime.now().toordinal())
