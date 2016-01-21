import feedparser
import requests


EVENTS_RSS_URL = "https://www.abdn.ac.uk/ims/seminars/rss.xml"
EVENTS_ICAL_URL = "https://www.abdn.ac.uk/ims/seminars/ical/{}/"

def fetch_events_as_ics():
    data = feedparser.parse(EVENTS_RSS_URL)

    # Extract the unique event id from rss event entries
    event_ids = [e['id'].split('/')[5] for e in data['entries']]

    # Concatenate the events
    calendar = "BEGIN:VCALENDAR\r\n"
    for event_id in event_ids:
        event_ical = requests.get(EVENTS_ICAL_URL.format(event_id))
        calendar += extract_event(event_ical)

    calendar += "END:VCALENDAR\r\n"

    return calendar

def extract_event(event_ical):
    """
    Remove the BEGIN:VCALENDAR and END:VCALENDAR lines
    so that we can concatenate the events
    """

    return event_ical.text.replace("BEGIN:VCALENDAR\r\n", "")\
        .replace("END:VCALENDAR\r\n", "")
