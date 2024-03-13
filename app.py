from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from flask_mobility import Mobility
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user

import func
from datetime import datetime

application = Flask(__name__)


application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)
application.app_context().push()
login_manager = LoginManager(application)
login_manager.login_view = 'login'
class Titles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(50),unique=True, nullable=False)
    title = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<Titles %r>' % self.path


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(Users).get(user_id)


class Users(db.Model, UserMixin):
    # __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(100))
    password_hash = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    color = db.Column(db.String(10))
    # logs = db.relationship('Logs', backref='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return "<Users %r>" % self.name


class Logs(db.Model):
    # __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    info = db.Column(db.String(300))
    date = db.Column(db.DateTime, default=datetime.utcnow())
    type = db.Column(db.String(10), nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # user = db.relationship("User", back_populates="company")
    user_name = db.Column(db.String(100), nullable=False)
    user_color = db.Column(db.String(10), nullable=False)

    def get_color(self):
        if self.type == "success":
            return "#146B14"
        elif self.type == "error":
            return "#751515"
        elif self.type == "warning":
            return "#757315"

    def __repr__(self):
        return '<Log %r>' % self.id


Mobility(application)
application.secret_key = "Wx4w54bL*7Tzdez(Td;"
application.config['MAIL_SERVER'] = 'smtp.magnavis.ru'
application.config['MAIL_PORT'] = 587
application.config['MAIL_USE_TLS'] = True
application.config['MAIL_USE_SSL'] = False
# application.config['MAIL_USERNAME'] = 'akcarapko@gmail.com'
# application.config['MAIL_USERNAME'] = 'inforder@magnavis.ru'
application.config['MAIL_USERNAME'] = 'siteclient@magnavis.ru'
application.config['MAIL_DEFAULT_SENDER'] = 'siteclient@magnavis.ru'
# application.config['MAIL_PASSWORD'] = 'RapsodiyaFenseret5'
# application.config['MAIL_PASSWORD'] = 'Kiloper=1224'
application.config['MAIL_PASSWORD'] = 'jG6qK9xK6awY6fS6'
mail = Mail(application)
mails = ['inforder@magnavis.ru', 'triikas@magnavis.ru']
# mails = ['triikas@magnavis.ru']


@application.route('/adm', methods=['post', 'get'])
@login_required
def adm():
    titles = Titles.query.order_by(Titles.id.desc()).all()
    logs = Logs.query.order_by(Logs.id.desc()).all()
    print(titles)
    if request.method == 'POST':
        type = request.form.get('type')
        if type == "add-news":
            title = request.form.get('title')
            path = request.form.get('path')
            data = request.form.get('data')
            img = request.form.get('img')
            img2 = request.form.get('img2')
            pb = request.form.get('pb')
            # p1 = request.form.get('p1')
            ps = []
            i = 1
            last = False
            while not last:
                p = request.form.get('p{}'.format(i))
                if p is not None:
                    i += 1
                    ps.append(p)
                else:
                    last = True
            print(title, path, data, img, pb, ps, type)
        elif type == "add-titles":
            title = request.form.get('title')
            path = request.form.get('path')
            if db.session.query(Titles).filter(Titles.path == path).first() == None:
                data = Titles(title=title, path=path)
                log = Logs(title="Добавлен заголовок (title)", info=(path+"|"+title), type="success", user_name=current_user.name, user_color=current_user.color)

                try:
                    db.session.add(data)
                    db.session.commit()
                except:
                    log.type = "error"
                    log.title = "Ошибка при добавлении заголовка (title)"
                try:
                    db.session.add(log)
                    db.session.commit()
                except:
                    return "ошибка логгирования, свяжитесь с разработчиком"
            else:
                log = Logs(title="Ошибка при добавлении заголовка (title)", info=(path + "|" + title), type="error",
                           user_name=current_user.name, user_color=current_user.color)
                try:
                    db.session.add(log)
                    db.session.commit()
                except:
                    return "ошибка логгирования, свяжитесь с разработчиком"
            return redirect("adm")
        elif type == "del-titles":
            path = request.form.get('path')
            try:
                title = db.session.query(Titles).filter(Titles.path == path).first()
                log = Logs(title="Удалён заголовок (title)", info=(path + "|" + title.title), type="warning",
                           user_name=current_user.name, user_color=current_user.color)
            except:
                log = Logs(title="Ошибка при удалении заголовка (title)", info=(path + "|"), type="error",
                           user_name=current_user.name, user_color=current_user.color)
                try:
                    db.session.add(log)
                    db.session.commit()
                except:
                    return "ошибка логгирования, свяжитесь с разработчиком"
                return redirect("adm")
            else:

                try:
                    data = db.session.query(Titles).filter(Titles.path == path).first()
                    db.session.delete(data)
                    db.session.commit()
                except:
                    log.type = "error"
                    log.title = "Ошибка при удалении заголовка (title)"
                try:
                    db.session.add(log)
                    db.session.commit()
                except:
                    return "ошибка логгирования, свяжитесь с разработчиком"
                return redirect("adm")
        elif type == "ch-titles":
            title = request.form.get('title')
            path = request.form.get('path')
            print(title, path)
            log = Logs(title="Иззменён заголовок (title)", info=(path + "|" + title), type="success",
                       user_name=current_user.name, user_color=current_user.color)
            try:
                ttl = db.session.query(Titles).filter(Titles.path == path).first()
                ttl.title = title
            except:
                log.type = "error"
                log.title = "Ошибка при изменении заголовка (title)"
                try:
                    db.session.add(log)
                    db.session.commit()
                except:
                    return "ошибка логгирования, свяжитесь с разработчиком"
                return redirect("adm")
            else:

                try:

                    db.session.merge(ttl)
                    db.session.commit()
                except:
                    log.type = "error"
                    log.title = "Ошибка при изменении заголовка (title)"
                try:
                    db.session.add(log)
                    db.session.commit()
                except:
                    return "ошибка логгирования, свяжитесь с разработчиком"
                return redirect("adm")

    return render_template('adm.html', titles=titles, logs=logs)


@application.route('/adm/in', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        mail = request.form.get('mail')
        password = request.form.get('pass')
        user = db.session.query(Users).filter(Users.email == mail).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('adm'))
        else:
            message = "Неверная почта или пароль"
    return render_template('in.html', message=message)



@application.route('/adm/out')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@application.route('/', methods=['post', 'get'])
def home():
    titles = db.session.query(Titles).filter(Titles.path=='home').first()
    # titles = Titles.query.all()
    print(titles)
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/home.html', titles=titles)
    else:
        return render_template('home.html', titles=titles)

@application.route('/yandex_d8918d0df7f73488.html', methods=['post', 'get'])
def webmaster():
    return render_template('yandex_d8918d0df7f73488.html')

@application.route('/contacts', methods=['post', 'get'])
def contacts():
    func.docs_update()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/contacts.html')
    else:
        return render_template('contacts.html')

@application.route('/directions', methods=['post', 'get'])
def directions():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/directions.html')
    else:
        return render_template('directions.html')

@application.route('/directions/china', methods=['post', 'get'])
def china():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/dir/china.html')
    else:
        return render_template('dir/china.html')


@application.route('/directions/oae', methods=['post', 'get'])
def oae():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/dir/oae.html')
    else:
        return render_template('dir/oae.html')


@application.route('/directions/russia', methods=['post', 'get'])
def russia():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/dir/ru.html')
    else:
        return render_template('dir/ru.html')


@application.route('/directions/turkey', methods=['post', 'get'])
def turkey():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/dir/trc.html')
    else:
        return render_template('dir/trc.html')


@application.route('/directions/india', methods=['post', 'get'])
def india():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/dir/ind.html')
    else:
        return render_template('dir/ind.html')


@application.route('/directions/skorea', methods=['post', 'get'])
def skorea():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/dir/sk.html')
    else:
        return render_template('dir/sk.html')


@application.route('/directions/hongkong', methods=['post', 'get'])
def hongkong():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/dir/hongkong.html')
    else:
        return render_template('dir/hongkong.html')

@application.route('/payment', methods=['post', 'get'])
def payment():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/payment.html')
    else:
        return render_template('payment.html')

@application.route('/services', methods=['post', 'get'])
def services():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/services.html')
    else:
        return render_template('services.html')



@application.route('/info', methods=['post', 'get'])
def info():
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/info.html')
    else:
        return render_template('info.html')


@application.route('/info/<string:pst>', methods=['post', 'get'])
def pt(pst):
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
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


@application.route('/info/shanhai', methods=['post', 'get'])
def shanhai():
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
                return redirect(url_for('mobile/news-vrem/shanhai'))
            else:
                return redirect(url_for('news-vrem/shanhai'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/news-vrem/shanhai'))
            else:
                return redirect(url_for('news-vrem/shanhai'))
    if request.MOBILE:
        return render_template('mobile/news-vrem/shanhai.html')
    else:
        return render_template('news-vrem/shanhai.html')


@application.route('/info/g4721', methods=['post', 'get'])
def g4721():
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
                return redirect(url_for('mobile/news-vrem/g4721'))
            else:
                return redirect(url_for('news-vrem/g4721'))
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        if ("noreply" or "no.reply" or "no-reply") in str(request.form.get('email')) or str(request.form.get('lovushka')) != "None" or (str(request.form.get('name')) or str(request.form.get('email')) or str(request.form.get('number'))) == "None":
            flash("Вы указали почту, на которую нельзя ответить")
        else:
            mail.send(msg)
            flash("Запрос отправлен")
            # print(str((request.form.get('email'))))
            if request.MOBILE:
                return redirect(url_for('mobile/news-vrem/g4721'))
            else:
                return redirect(url_for('news-vrem/g4721'))
    if request.MOBILE:
        return render_template('mobile/news-vrem/g4721.html')
    else:
        return render_template('news-vrem/g4721.html')


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
