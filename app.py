import logging

from flask import Flask, send_from_directory
from main.utils import views_blueprint
from load.views import loader_blueprint


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(views_blueprint)
app.register_blueprint(loader_blueprint)

logging.basicConfig(filename='basic.log', level=logging.INFO, encoding='utf-8')


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()
