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
mails = ['sales1@magnavis.ru', 'cargo@magnavis.ru', 'marwy@magnavis.ru', 'pvl@magnavis.ru', 'andr@magnavis.ru']



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

@application.route('/yandex_d8918d0df7f73488.html', methods=['post', 'get'])
def webmaster():
    return render_template('yandex_d8918d0df7f73488.html')

@application.route('/contacts', methods=['post', 'get'])
def contacts():
    func.docs_update()
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

@application.route('/directions', methods=['post', 'get'])
def directions():
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
                return redirect(url_for('mobile/directions'))
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
                return redirect(url_for('mobile/directions'))
            else:
                return redirect(url_for('directions'))
    if request.MOBILE:
        return render_template('mobile/directions.html')
    else:
        return render_template('directions.html')

@application.route('/directions/china', methods=['post', 'get'])
def china():
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
                return redirect(url_for('mobile/dir/china'))
            else:
                return redirect(url_for('dir/china'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/dir/china'))
            else:
                return redirect(url_for('dir/china'))
    if request.MOBILE:
        return render_template('mobile/dir/china.html')
    else:
        return render_template('dir/china.html')

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

@application.route('/info', methods=['post', 'get'])
def info():
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
                return redirect(url_for('mobile/info'))
            else:
                return redirect(url_for('info'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/info'))
            else:
                return redirect(url_for('prob'))
    if request.MOBILE:
        return render_template('mobile/info.html')
    else:
        return render_template('info.html')


@application.route('/info/prob', methods=['post', 'get'])
def prob():
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
                return redirect(url_for('mobile/news-vrem/prob'))
            else:
                return redirect(url_for('news-vrem/prob'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/news-vrem/prob'))
            else:
                return redirect(url_for('news-vrem/prob'))
    if request.MOBILE:
        return render_template('mobile/news-vrem/prob.html')
    else:
        return render_template('news-vrem/prob.html')


@application.route('/info/suparna', methods=['post', 'get'])
def suparna():
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
                return redirect(url_for('mobile/news-vrem/suparna'))
            else:
                return redirect(url_for('news-vrem/suparna'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/news-vrem/suparna'))
            else:
                return redirect(url_for('news-vrem/suparna'))
    if request.MOBILE:
        return render_template('mobile/news-vrem/suparna.html')
    else:
        return render_template('news-vrem/suparna.html')


@application.route('/info/sutochnie', methods=['post', 'get'])
def sutochnie():
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
                return redirect(url_for('mobile/news-vrem/sutochnie'))
            else:
                return redirect(url_for('news-vrem/sutochnie'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/news-vrem/sutochnie'))
            else:
                return redirect(url_for('news-vrem/sutochnie'))
    if request.MOBILE:
        return render_template('mobile/news-vrem/sutochnie.html')
    else:
        return render_template('news-vrem/sutochnie.html')


@application.route('/info/agro', methods=['post', 'get'])
def agro():
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
                return redirect(url_for('mobile/news-vrem/agro'))
            else:
                return redirect(url_for('news-vrem/agro'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/news-vrem/agro'))
            else:
                return redirect(url_for('news-vrem/agro'))
    if request.MOBILE:
        return render_template('mobile/news-vrem/agro.html')
    else:
        return render_template('news-vrem/agro.html')


@application.route('/info/garant', methods=['post', 'get'])
def garant():
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
                return redirect(url_for('mobile/news-vrem/garant'))
            else:
                return redirect(url_for('news-vrem/garant'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/news-vrem/garant'))
            else:
                return redirect(url_for('news-vrem/garant'))
    if request.MOBILE:
        return render_template('mobile/news-vrem/garant.html')
    else:
        return render_template('news-vrem/garant.html')



@application.route('/info/il96', methods=['post', 'get'])
def il96():
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
                return redirect(url_for('mobile/news-vrem/il96'))
            else:
                return redirect(url_for('news-vrem/il96'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/news-vrem/il96'))
            else:
                return redirect(url_for('news-vrem/il96'))
    if request.MOBILE:
        return render_template('mobile/news-vrem/il96.html')
    else:
        return render_template('news-vrem/il96.html')


@application.route('/info/haynan', methods=['post', 'get'])
def haynan():
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
                return redirect(url_for('mobile/news-vrem/haynan'))
            else:
                return redirect(url_for('news-vrem/haynan'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/news-vrem/haynan'))
            else:
                return redirect(url_for('news-vrem/haynan'))
    if request.MOBILE:
        return render_template('mobile/news-vrem/haynan.html')
    else:
        return render_template('news-vrem/haynan.html')


@application.route('/info/kalin', methods=['post', 'get'])
def kalin():
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
                return redirect(url_for('mobile/news-vrem/kalin'))
            else:
                return redirect(url_for('news-vrem/kalin'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/news-vrem/kalin'))
            else:
                return redirect(url_for('news-vrem/kalin'))
    if request.MOBILE:
        return render_template('mobile/news-vrem/kalin.html')
    else:
        return render_template('news-vrem/kalin.html')

@application.route('/info/spravochnik', methods=['post', 'get'])
def spravochnik():
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
                return redirect(url_for('mobile/news-vrem/spravochnik'))
            else:
                return redirect(url_for('news-vrem/spravochnik'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/news-vrem/spravochnik'))
            else:
                return redirect(url_for('news-vrem/spravochnik'))
    if request.MOBILE:
        return render_template('mobile/news-vrem/spravochnik.html')
    else:
        return render_template('news-vrem/spravochnik.html')


@application.route('/info/rgd', methods=['post', 'get'])
def rgd():
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
                return redirect(url_for('mobile/news-vrem/rgd'))
            else:
                return redirect(url_for('news-vrem/rgd'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/news-vrem/rgd'))
            else:
                return redirect(url_for('news-vrem/rgd'))
    if request.MOBILE:
        return render_template('mobile/news-vrem/rgd.html')
    else:
        return render_template('news-vrem/rgd.html')


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
        return render_template('mobile/about.html', numbers=numbers)
    else:
        return render_template('about.html', numbers=numbers)


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
