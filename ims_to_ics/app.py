from flask import Flask
from flask import Response
from .config_parser import Config
from .database import Database

config = Config()
app = Flask(__name__)


@app.route('/ims_seminars/')
def ims_seminars_as_ics():
    db = Database()

    return Response(db.get_ics(), mimetype="text/calendar")

if __name__ == '__main__':
    app.run()
