from flask import Flask
from flask import Response
from flask.ext.redis import FlaskRedis
from redis import Redis
from config_parser import Config

config = Config()
app = Flask(__name__)

redis_store = FlaskRedis.from_custom_provider(Redis(host=config.get('REDIS', 'Host'),
                                                    port=config.get('REDIS', 'Port'),
                                                    db=config.get('REDIS', 'Db')), app)


@app.route('/ims_seminars/')
def ims_seminars_as_ics():
    ics = redis_store.get('calendar').decode('utf-8')

    return Response(ics, mimetype="text/calendar")

if __name__ == '__main__':
    app.run()
