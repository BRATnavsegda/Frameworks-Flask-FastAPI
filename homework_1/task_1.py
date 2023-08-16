from flask import Flask, render_template

import hw_text_storage as storage

app = Flask(__name__)


@app.route("/")
def index():
    context = storage.index_tasks

    return render_template("index.html", **context)


@app.route("/about/")
def about():
    context = storage.about_text

    return render_template("flash_name.html", **context)


@app.route("/contacts/")
def contacts():
    context = storage.contacts_text

    return render_template("contacts.html", **context)


@app.route("/news/")
def news():
    context = storage.news_content

    return render_template("name_age.html", **context)


@app.route("/store/")
def store_categories():
    context = storage.store_categories

    return render_template("correct_age.html", **context)


@app.route("/store/<page>/")
def store_page(page):
    context = storage.store_pages[page]

    return render_template("store_page.html", **context)




if __name__ == '__main__':
    app.run(debug=True)

