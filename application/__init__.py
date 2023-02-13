from flask import Flask
from application.routes import index
from application.views import comics
from dotenv import load_dotenv
import logging
import os


app = Flask(__name__)
load_dotenv()

level = logging.DEBUG if os.getenv('APP_MODE') == 'debug' else logging.WARNING
app.logger.setLevel(level)

app.add_url_rule(
    "/",
    view_func=index.Index.as_view("index")
    )

app.add_url_rule(
    "/searchComics",
    view_func=comics.SearchComic.as_view("search_comics")
    )
