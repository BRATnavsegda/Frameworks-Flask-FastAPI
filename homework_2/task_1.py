from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session
import secrets
import hw_text_storage as storage

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route("/", methods=['GET', 'POST'])
@app.route("/index/", methods=['GET', 'POST'])
def index():
    context = storage.index_tasks
    if 'username' in session:
        print(f'Привет, {session["username"]}')

    return render_template("index.html", **context)


@app.route("/contacts/")
def contacts():
    context = storage.contacts_text

    return render_template("contacts.html", **context)


@app.route("/name_age/", methods=['GET', 'POST'])
def name_age():
    context = storage.name_age_content
    if request.method == 'POST':
        if int(request.form.get('age')) >= 18:
            return redirect(url_for('correct_age'))
        else:
            return redirect(url_for('age_error'))
    return render_template("name_age.html", **context)


@app.route("/correct_age/")
def correct_age():
    context = storage.cor_age

    return render_template("correct_age.html", **context)


@app.route("/age_error/")
def age_error():
    context = storage.err_age

    return render_template("correct_age.html", **context)


@app.route('/num_square/', methods=['GET', 'POST'])
def num_square():
    context = storage.num_square
    if request.method == 'POST':
        res = str(int(request.form.get('number')) ** 2)
        num = request.form.get('number')
        return render_template('number_squared.html', num=num, res=res)

    return render_template("num_square.html", **context)


@app.route('/number_squared/<num>-<res>')
def number_squared():
    return render_template("number_squared.html")


@app.route("/flash_hello/", methods=['GET', 'POST'])
def flash_hello():
    context = storage.flash_text
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('flash_hello'))
        # Обработка данных формы
        flash(f'Форма успешно отправлена! Привет, {request.form["name"]}!', 'success')
        return redirect(url_for('flash_hello'))
    return render_template('flash_hello.html', **context)


@app.route('/authorize/', methods=['GET', 'POST'])
def authorize():
    context = storage.auth
    if request.method == 'POST':
        # response = make_response(render_template('auth_success.html', **context))
        # response.set_cookie('name', request.form.get("name"))
        # response.set_cookie('email', request.form["email"])
        # return response
        session['username'] = request.form.get('username')
        session['user_email'] = request.form.get('user_email')
        return redirect(url_for('index'))

    return render_template('authorize.html', **context)


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
