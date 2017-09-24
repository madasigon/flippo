from flask import Flask
from flask_redis import FlaskRedis


app = Flask(__name__)
app.config['REDIS_URL'] = 'redis://:@localhost:6379/0'  # konfiguralhato
redis_store = FlaskRedis(app)

import views
