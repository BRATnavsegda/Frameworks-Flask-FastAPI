import secrets
from flask import Flask, render_template, request, flash, redirect, url_for
from sqlalchemy import or_

from hw3_models import db, Students, Faculties, Books, Authors, FormForTask4, DataForTask4
import hw_3_text_storage as storage
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# secret_key = b'97b3c2a38768bfbd184ca8e63d5fe2bb144470985bad9911e79e832ce'
app.config['SECRET_KEY'] = b'97b3c2a38768bfbd184ca8e63d5fe2'
db.init_app(app)
csrf = CSRFProtect(app)
app.secret_key = b'97b3c2a38768bfbd184ca8e63d5fe2bb144470985bad9911e79e832ce'


@app.route("/")
@app.route("/index/", methods=['GET', 'POST'])
def index():
    context = storage.index_tasks

    return render_template("index.html", **context)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('created db')


@app.route('/students/')
def students():
    res_students = Students.query.all()
    res_faculties = Faculties.query.all()
    context = {'res_students': res_students,
               'res_faculties': res_faculties,
               }
    return render_template('students.html', **context)


@app.cli.command('fill_students')
def fill_students():
    for i in range(10):
        student = Students(name=f'Student {i}', soname=f'Student soname{i**2}',
                           age=18+i, group=f'Group {101+i}')
        db.session.add(student)
        db.session.commit()
    print('students was added')


@app.cli.command('fill_faculty')
def fill_faculty():
    for i in range(5):
        faculty = Faculties(faculty_name=f'faculty {i}')
        db.session.add(faculty)
        db.session.commit()
    print('Faculties was added')


@app.route('/books/')
def books():
    res_books = Books.query.all()
    res_authors = Authors.query.all()
    context = {'res_books': res_books,
               'res_authors': res_authors,
               }
    return render_template('books.html', **context)


@app.cli.command('fill_books')
def fill_books():
    for i in range(1, 6):
        book = Books(name=f'Book {i}',
                     publication=f'{i}.0{i}.198{i}',
                     copies=i**3)
        db.session.add(book)
    db.session.commit()
    print('books was added')


@app.cli.command('fill_authors')
def fill_authors():
    for i in range(5):
        author = Authors(author_name=f'author {i}',
                         author_soname=f'author soname {i}',
                         )
        db.session.add(author)
    db.session.commit()
    print('Authors was added')

# "Задание №4",

#  Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
#  содержать следующие поля:
#  ○ Имя пользователя (обязательное поле)
#  ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
#  ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
#  ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
#  После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
#  и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
#  заполнено или данные не прошли валидацию, то должно выводиться соответствующее
#  сообщение об ошибке.
#  Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
#  базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
#  об ошибке.


@app.route('/login_task4/', methods=['GET', 'POST'])
@csrf.exempt
def login_task4():
    form = FormForTask4()
    if request.method == 'POST' and form.validate():

        existing_user = DataForTask4.query.filter(
            or_(DataForTask4.name == form.name.data, DataForTask4.email == form.email.data)).first()

        if existing_user:
            flash('Пользователь с таким именем или электронной почтой уже зарегистрирован!', 'danger')
            return redirect(url_for("login_task4", form=form))

        else:
            new_user = DataForTask4(name=form.name.data,
                                    email=form.email.data,
                                    password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('login_task4.html', form=form)

