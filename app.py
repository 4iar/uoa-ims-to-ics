from flask import Flask
from flask import Response
from flask.ext.redis import FlaskRedis

app = Flask(__name__)

redis_store = FlaskRedis(app)


@app.route('/ims_seminars/')
def ims_seminars_as_ics():
    ics = redis_store.get('calendar').decode('utf-8')

    return Response(ics, mimetype="text/calendar")

if __name__ == '__main__':
    app.run()
