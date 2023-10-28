from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from flask_mobility import Mobility
import func

application = Flask(__name__)
Mobility(application)
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
mails = ['sales1@magnavis.ru', 'cargo@magnavis.ru', 'marwy@magnavus.ru', 'pvl@magnavis.ru', 'andr@magnavis.ru']

@application.route('/', methods=['post', 'get'])
def home():
    print("fgh: ", str(request.MOBILE))
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        # msg = Message("Запрос с magnavis.ru", recipients=['q1113p@mail.ru'])
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        lovushka = request.form.get('lovushka')
        kod = request.form.get('kod')
        if str(request.form.get('kod')) != "None":
            flash("Груз не найден")
            # if request.MOBILE:
            #     return redirect(url_for('mobile/home'))
            # else:
            return redirect(url_for('home'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Неверные данные")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # if request.MOBILE:
            #     return redirect(url_for('mobile/home'))
            # else:
            return redirect(url_for('home'))
    if request.MOBILE:
        return render_template('mobile/home.html')
    else:
        return render_template('home.html')

@application.route('/contacts', methods=['post', 'get'])
def contacts():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        # msg = Message("Запрос с magnavis.ru", recipients=['q1113p@mail.ru'])
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        lovushka = request.form.get('lovushka')
        kod = request.form.get('kod')
        if str(request.form.get('kod')) != "None":
            flash("Груз не найден")
            if request.MOBILE:
                return redirect(url_for('mobile/contacts'))
            else:
                return redirect(url_for('contacts'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/contacts'))
            else:
                return redirect(url_for('contacts'))
    if request.MOBILE:
        return render_template('mobile/contacts.html')
    else:
        return render_template('contacts.html')

@application.route('/payment', methods=['post', 'get'])
def payment():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        # msg = Message("Запрос с magnavis.ru", recipients=['q1113p@mail.ru'])
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        lovushka = request.form.get('lovushka')
        kod = request.form.get('kod')
        if str(request.form.get('kod')) != "None":
            flash("Груз не найден")
            if request.MOBILE:
                return redirect(url_for('mobile/payment'))
            else:
                return redirect(url_for('payment'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/payment'))
            else:
                return redirect(url_for('payment'))
    if request.MOBILE:
        return render_template('mobile/payment.html')
    else:
        return render_template('payment.html')

@application.route('/services', methods=['post', 'get'])
def services():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        # msg = Message("Запрос с magnavis.ru", recipients=['q1113p@mail.ru'])
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        lovushka = request.form.get('lovushka')
        kod = request.form.get('kod')
        if str(request.form.get('kod')) != "None":
            flash("Груз не найден")
            if request.MOBILE:
                return redirect(url_for('mobile/services'))
            else:
                return redirect(url_for('services'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/services'))
            else:
                return redirect(url_for('services'))
    if request.MOBILE:
        return render_template('mobile/services.html')
    else:
        return render_template('services.html')

@application.route('/about', methods=['post', 'get'])
def about():
    numbers = func.numbers()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        # msg = Message("Запрос с magnavis.ru", recipients=['q1113p@mail.ru'])
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        lovushka = request.form.get('lovushka')
        kod = request.form.get('kod')
        if str(request.form.get('kod')) != "None":
            flash("Груз не найден")
            if request.MOBILE:
                return redirect(url_for('mobile/about'))
            else:
                return redirect(url_for('about'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            # mail.send(msg)               //механизм формы тут не нужен
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/about'))
            else:
                return redirect(url_for('about'))
    if request.MOBILE:
        return render_template('mobile/about.html')
    else:
        return render_template('about.html', numbers=numbers)


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=False)
