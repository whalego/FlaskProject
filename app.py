# -*- coding:utf-8 -*-

from flask import Flask, render_template
from loggingmodule import init_logging

app = Flask(__name__)

test_data = [
    [1, "a", "あ"],
    [2, "b", "い"],
    [3, "c", "う"],
    [4, "d", "え"],
    [5, "e", "お"],
    [6, "f", "か"],
    [7, "g", "き"],
    [8, "h", "く"],
    [9, "j", "け"],
    [10, "k", "こ"],
    [11, "l", "さ"],
    [12, "m", "し"],
    [13, "n", "す"],
    [14, "o", "せ"],
    [15, "p", "そ"],
    [16, "q", "た"],
    [17, "r", "ち"],
    [18, "s", "つ"],
    [19, "t", "て"],
    [20, "u", "と"],
]

test_user = ["kujira_go", "asd_go"]

logger = init_logging(__name__)


@app.route("/")
def index():

    logger.info("View main page")

    return render_template("/index.html",
                           title="テスト用ページ",
                           user=test_user,
                           message=test_data,
                           image_url="/static/images/20181010_001.jpg"
                           )


if __name__ == "__main__":
    app.run()


