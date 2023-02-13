from flask import Flask
from application.routes import index
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()

app.add_url_rule("/", view_func=index.Index.as_view("index"))
