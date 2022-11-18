from flask import Flask
import logging
from api_endpoints.view import api_blueprint
from bookmarks.view import bookmarks_blueprint
from handlers.view import handlers_blueprint
from main.view import main_blueprint
from search.view import search_blueprint
from tags.view import tags_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(filename="logs/api.log", level=logging.INFO, format=FORMAT)

app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(handlers_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(tags_blueprint)
app.register_blueprint(bookmarks_blueprint)


if __name__ == '__main__':
    app.run()
