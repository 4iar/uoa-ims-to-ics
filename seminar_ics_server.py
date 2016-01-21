from flask import Flask
from seminar_parser import fetch_events_as_ics

app = Flask(__name__)

@app.route('/ims_seminars/')
def ims_seminars_as_ics():
    return fetch_events_as_ics()

if __name__ == '__main__':
    app.run()
