from pathlib import PurePath, Path

from flask import Flask, url_for, request, render_template
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Экранирование, защита от скриптов в строке браузера
@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'

@app.route('/<path:file>/')
def get_file(file):
    print(file)
    return f'Ваш файл находится в: {escape(file)}! '


@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок.<br>'
    return f'{text} {request.args}'

# url_for('static',
# filename='css/bootstrap.css')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('submit.html')

# @app.get('/submit')
# def submit_get():
#   return render_template('form.html')
#
# @app.post('/submit')
# def submit_post():
#   name = request.form.get('name')
#   return f'Hello {name}!'


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


if __name__ == '__main__':

    app.run(debug=True)
