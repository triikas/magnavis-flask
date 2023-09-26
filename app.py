from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

application = Flask(__name__)
application.secret_key = "Wx4w54bL*7Tzdez(Td;"
application.config['MAIL_SERVER'] = 'smtp.magnavis.ru'
application.config['MAIL_PORT'] = 587
application.config['MAIL_USE_TLS'] = True
application.config['MAIL_USE_SSL'] = False
# application.config['MAIL_USERNAME'] = 'akcarapko@gmail.com'
application.config['MAIL_USERNAME'] = 'inforder@magnavis.ru'
application.config['MAIL_DEFAULT_SENDER'] = 'inforder@magnavis.ru'
# application.config['MAIL_PASSWORD'] = 'RapsodiyaFenseret5'
application.config['MAIL_PASSWORD'] = 'Kiloper=1224'
mail = Mail(application)

@application.route('/', methods=['post', 'get'])
def home():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=['sales1@magnavis.ru', 'sales2@magnavis.ru', 'cargo@magnavis.ru'])
        # msg = Message("Запрос с magnavis.ru", recipients=['q1113p@mail.ru'])
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        lovushka = request.form.get('lovushka')
        kod = request.form.get('kod')
        if str(request.form.get('kod')) != "None":
            flash("Груз не найден")
            return redirect(url_for('home'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Неверные данные")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            # print(str((request.form.get('kod'))))
            return redirect(url_for('home'))

    return render_template('home.html')

@application.route('/contacts', methods=['post', 'get'])
def contacts():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=['sales1@magnavis.ru', 'sales2@magnavis.ru', 'cargo@magnavis.ru'])
        # msg = Message("Запрос с magnavis.ru", recipients=['q1113p@mail.ru'])
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        lovushka = request.form.get('lovushka')
        kod = request.form.get('kod')
        if str(request.form.get('kod')) != "None":
            flash("Груз не найден")
            return redirect(url_for('contacts'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            return redirect(url_for('contacts'))
    return render_template('contacts.html')

@application.route('/payment', methods=['post', 'get'])
def payment():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=['sales1@magnavis.ru', 'sales2@magnavis.ru', 'cargo@magnavis.ru'])
        # msg = Message("Запрос с magnavis.ru", recipients=['q1113p@mail.ru'])
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        lovushka = request.form.get('lovushka')
        kod = request.form.get('kod')
        if str(request.form.get('kod')) != "None":
            flash("Груз не найден")
            return redirect(url_for('payment'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            return redirect(url_for('payment'))
    return render_template('payment.html')

@application.route('/services', methods=['post', 'get'])
def services():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=['sales1@magnavis.ru', 'sales2@magnavis.ru', 'cargo@magnavis.ru'])
        # msg = Message("Запрос с magnavis.ru", recipients=['q1113p@mail.ru'])
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        lovushka = request.form.get('lovushka')
        kod = request.form.get('kod')
        if str(request.form.get('kod')) != "None":
            flash("Груз не найден")
            return redirect(url_for('services'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            return redirect(url_for('services'))
    return render_template('services.html')

@application.route('/about', methods=['post', 'get'])
def about():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=['sales1@magnavis.ru', 'sales2@magnavis.ru', 'cargo@magnavis.ru'])
        # msg = Message("Запрос с magnavis.ru", recipients=['q1113p@mail.ru'])
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        lovushka = request.form.get('lovushka')
        kod = request.form.get('kod')
        if str(request.form.get('kod')) != "None":
            flash("Груз не найден")
            return redirect(url_for('about'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            return redirect(url_for('about'))
    return render_template('about.html')


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=False)
