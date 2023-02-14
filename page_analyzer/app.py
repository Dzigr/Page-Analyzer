"""Flask app module"""
from dotenv import load_dotenv
from flask import (
    Flask,
    flash,
    get_flashed_messages,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)
import psycopg2
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/urls', methods=['GET'])
def show_urls():
    return render_template('urls.html')


@app.route('/urls', methods=['POST'])
def post_url():
    pass


@app.route('/urls/<int:id>', methods=['GET'])
def show_url(id):
    return render_template('url_detail.html')


@app.route('/urls/<int:id>/checks', methods=['POST'])
def check_url(id):
    pass


@app.errorhandler(404)
def show_error_page(error):
    return render_template(
        'page404.html',
        title='Страница не найдена',
    )
