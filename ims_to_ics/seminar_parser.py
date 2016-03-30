import feedparser
import requests


EVENTS_RSS_URL = "https://www.abdn.ac.uk/ims/seminars/rss.xml"
EVENTS_ICAL_URL = "https://www.abdn.ac.uk/ims/seminars/ical/{}/"


def get_event_ids():
    """
    GET the events RSS and extract IDs for all events.
    """
    rss_page = requests.get(EVENTS_RSS_URL).text
    data = feedparser.parse(rss_page)

    # Extract the unique event id from rss event entries
    return [e['id'].split('/')[5] for e in data['entries']]

def fetch_events_as_ics():
    event_ids = get_event_ids()

    calendar = "BEGIN:VCALENDAR\r\n"
    for event_id in event_ids:
        # GET the ics file using the unique event ID (from get_event_ids)
        # then concat the ics files together

        event_ical = requests.get(EVENTS_ICAL_URL.format(event_id)).text
        calendar += extract_event(event_ical)

    calendar += "END:VCALENDAR\r\n"

    return calendar

def extract_event(event_ical):
    """
    Remove the BEGIN:VCALENDAR and END:VCALENDAR lines
    so that we can concatenate the events
    """

    return event_ical.replace("BEGIN:VCALENDAR\r\n", "")\
        .replace("END:VCALENDAR\r\n", "")
