from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '3b81a7164a731c013a39bcdad657becb'

from main import routes
