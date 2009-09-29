# -*- coding:utf-8 -*-

from flask import Flask, render_template, request
from loggingmodule import init_logging
from DBconnection import DbController

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
    [9, "j", "け"]
]

test_user = ["kujira_go", "asd_go"]

logger = init_logging(__name__)


@app.route("/")
def index():

    logger.info("View main page")
    db = DbController()
    data = db.check_data()
    del db
    return render_template("/contents/index.html",
                           title="テスト用ページ",
                           user=test_user,
                           message=test_data,
                           data=data,
                           page="/form_page",
                           image_url="/static/images/201916.png"
                           )


@app.route("/form_page")
def form_page():
    logger.info("View form page")

    return render_template("/contents/form_page.html",
                           title="form_page",
                           user=test_user
                           )


@app.route("/confirm_page", methods=["POST", "GET"])
def confirm_page():
    logger.info("View add page")
    if request.method == "POST":

        user_name = request.form["user_name"]
        image = request.form["image"]
        category = request.form["category"]
        content = request.form["content"]
        result = [user_name, image, category, content]
        db = DbController()
        db.insert_record(username=user_name, image=image, category=category, content=content)
        del db
        return render_template("/contents/confirm_page.html",
                               title="confirm",
                               user=test_user,
                               result=result
                               )
    # if request.method == "GET":
    #     return render_template("/contents/confirm_page.html")


if __name__ == "__main__":
    app.run()


