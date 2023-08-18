from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

db = SQLAlchemy()


# В таблице "Факультеты" должны быть следующие поля: id и название
# факультета.

class Faculties(db.Model):
    faculty = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(30), nullable=False)
    faculty_students = db.relationship('Students', backref='author', lazy=True)


# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
# возраст, пол, группа и id факультета.

class Students(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    soname = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Boolean, default=True)
    group = db.Column(db.Integer, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey(Faculties.faculty), default=1)


# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.


class Authors(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(30), nullable=False)
    author_soname = db.Column(db.String(30), nullable=False)
    author_books = db.relationship('Books', backref='author', lazy=True)


# В таблице "Книги" должны быть следующие поля: id, название,
# год издания, количество экземпляров и id автора.

class Books(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    publication = db.Column(db.String(30), nullable=False)
    copies = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey(Authors.author_id), default=1)


class FormForTask4(FlaskForm):
    name = StringField('Name', validators=[DataRequired()],
                       render_kw={'class': 'form-control',
                                  'placeholder': 'Введите ваше имя'})
    email = StringField('Email', validators=[DataRequired(), Email()],
                        render_kw={'class': 'form-control',
                                   'placeholder': 'Введите адрес электронной почты'})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)],
                             render_kw={'class': 'form-control',
                                        'placeholder': 'Введите пароль'})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')],
                                     render_kw={'class': 'form-control',
                                                'placeholder': 'Подтвердите пароль'})

    def validate_name(self, name):
        excluded_chars = " *?!'^+%&amp;/()=}][{$#"
        for char in self.name.data:
            if char in excluded_chars:
                raise ValidationError(
                    f"Символы {excluded_chars} в имени пользователя недопустимы.")

    def validate_password(self, password):
        has_digit = False
        has_letter = False
        for char in self.password.data:
            if char.isdigit():
                has_digit = True
            elif char.isalpha():
                has_letter = True
            if has_digit and has_letter:
                break
        raise ValidationError(
            f"Пароль должен содержать хотя бы одну букву и одну цифру")


class DataForTask4(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
