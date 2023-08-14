from flask import Flask

app = Flask(__name__)


@app.route('/')
def intro():
    return 'Привет незнакомец!'
    # return 42 (возвращать только строки)


@app.route('/Николай/')
@app.route('/Ник/')
@app.route('/Коля/')
def nik():
    return 'Привет Николай!'


@app.route('/Roman/')
def roman():
    return 'Привет Roman!'


if __name__ == '__main__':
    app.run()

# запуск из командной строки - flask --app .\lesson_1\app_1.py run
