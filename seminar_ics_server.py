from flask import Flask
from flask import Response
from seminar_parser import fetch_events_as_ics

app = Flask(__name__)


@app.route('/ims_seminars/')
def ims_seminars_as_ics():
    ics = fetch_events_as_ics()

    return Response(ics, mimetype="text/calendar")

if __name__ == '__main__':
    app.run()
