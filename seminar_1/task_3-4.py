# Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/sum/<int:num1>-<int:num2>/')
def sum_num(num1, num2):
    return f'{num1 + num2}'


@app.route('/str/<string>/')
def str_len(string):
    return f'{len(string)}'


if __name__ == '__main__':
    app.run(debug=True)
