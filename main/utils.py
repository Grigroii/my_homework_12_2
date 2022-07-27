import logging

from flask import Blueprint, render_template, request
from functions import search_by_word
from json import JSONDecodeError
views_blueprint = Blueprint('views_blueprint', __name__, template_folder='templates')

@views_blueprint.route('/')
def main_page():
    return render_template('index.html')

@views_blueprint.route('/search/')
def search_posts():
    search = request.args.get('s')
    logging.info("Выполняю поиск")
    try:
        posts = search_by_word(search)
    except FileNotFoundError:
        return "Файл не найден"
    except JSONDecodeError:
        return "Невалидный файл"
    return render_template('post_list.html', posts=posts, search=search)
