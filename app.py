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
    path = db.Column(db.String(150),unique=True, nullable=False)
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
    titles = db.session.query(Titles).filter(Titles.path=='https://magnavis.ru').first()
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
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/contacts').first()
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
        return render_template('mobile/contacts.html', titles=titles)
    else:
        return render_template('contacts.html', titles=titles)

@application.route('/directions', methods=['post', 'get'])
def directions():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/directions').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/directions.html', titles=titles)
    else:
        return render_template('directions.html', titles=titles)

@application.route('/directions/china', methods=['post', 'get'])
def china():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/directions/china').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/dir/china.html', titles=titles)
    else:
        return render_template('dir/china.html', titles=titles)


@application.route('/directions/oae', methods=['post', 'get'])
def oae():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/directions/oae').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/dir/oae.html', titles=titles)
    else:
        return render_template('dir/oae.html', titles=titles)


@application.route('/directions/russia', methods=['post', 'get'])
def russia():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/directions/russia').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/dir/ru.html', titles=titles)
    else:
        return render_template('dir/ru.html', titles=titles)


@application.route('/directions/turkey', methods=['post', 'get'])
def turkey():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/directions/turkey').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/dir/trc.html', titles=titles)
    else:
        return render_template('dir/trc.html', titles=titles)


@application.route('/directions/india', methods=['post', 'get'])
def india():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/directions/india').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/dir/ind.html', titles=titles)
    else:
        return render_template('dir/ind.html', titles=titles)


@application.route('/directions/skorea', methods=['post', 'get'])
def skorea():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/directions/skorea').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/dir/sk.html', titles=titles)
    else:
        return render_template('dir/sk.html', titles=titles)


@application.route('/directions/hongkong', methods=['post', 'get'])
def hongkong():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/directions/hongkong').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/dir/hongkong.html', titles=titles)
    else:
        return render_template('dir/hongkong.html', titles=titles)

@application.route('/payment', methods=['post', 'get'])
def payment():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/directions/hongkong').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/payment.html', titles=titles)
    else:
        return render_template('payment.html', titles=titles)

@application.route('/services', methods=['post', 'get'])
def services():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/services').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/services.html', titles=titles)
    else:
        return render_template('services.html', titles=titles)



@application.route('/info', methods=['post', 'get'])
def info():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/info').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/info.html', titles=titles)
    else:
        return render_template('info.html', titles=titles)


@application.route('/info/<string:pst>', methods=['post', 'get'])
def pt(pst):
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/info/{}'.format(pst)).first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/info.html', titles=titles)
    else:
        return render_template('info.html', titles=titles)


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
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/info/suparna').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/news-vrem/suparna.html', titles=titles)
    else:
        return render_template('news-vrem/suparna.html', titles=titles)


@application.route('/info/msc-spb', methods=['post', 'get'])
def msc_spb():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/info/msc-spb').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/news-vrem/msc-spb.html', titles=titles)
    else:
        return render_template('news-vrem/msc-spb.html', titles=titles)


@application.route('/info/shanhai', methods=['post', 'get'])
def shanhai():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/info/shanhai').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/news-vrem/shanhai.html', titles=titles)
    else:
        return render_template('news-vrem/shanhai.html', titles=titles)


@application.route('/info/g4721', methods=['post', 'get'])
def g4721():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/info/g4721').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/news-vrem/g4721.html', titles=titles)
    else:
        return render_template('news-vrem/g4721.html', titles=titles)


@application.route('/info/sutochnie', methods=['post', 'get'])
def sutochnie():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/info/sutochnie').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/news-vrem/sutochnie.html', titles=titles)
    else:
        return render_template('news-vrem/sutochnie.html', titles=titles)


@application.route('/info/agro', methods=['post', 'get'])
def agro():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/info/agro').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/news-vrem/agro.html', titles=titles)
    else:
        return render_template('news-vrem/agro.html', titles=titles)


@application.route('/info/garant', methods=['post', 'get'])
def garant():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/info/garant').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/news-vrem/garant.html', titles=titles)
    else:
        return render_template('news-vrem/garant.html', titles=titles)



@application.route('/info/il96', methods=['post', 'get'])
def il96():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/info/garant').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/news-vrem/il96.html', titles=titles)
    else:
        return render_template('news-vrem/il96.html', titles=titles)


@application.route('/info/haynan', methods=['post', 'get'])
def haynan():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/info/haynan').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/news-vrem/haynan.html', titles=titles)
    else:
        return render_template('news-vrem/haynan.html', titles=titles)


@application.route('/info/kalin', methods=['post', 'get'])
def kalin():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/info/kalin').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/news-vrem/kalin.html', titles=titles)
    else:
        return render_template('news-vrem/kalin.html', titles=titles)

@application.route('/info/spravochnik', methods=['post', 'get'])
def spravochnik():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/info/spravochnik').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/news-vrem/spravochnik.html', titles=titles)
    else:
        return render_template('news-vrem/spravochnik.html', titles=titles)


@application.route('/info/rgd', methods=['post', 'get'])
def rgd():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/info/rgd').first()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/news-vrem/rgd.html', titles=titles)
    else:
        return render_template('news-vrem/rgd.html', titles=titles)


@application.route('/about', methods=['post', 'get'])
def about():
    titles = db.session.query(Titles).filter(Titles.path == 'https://magnavis.ru/about').first()
    numbers = func.numbers()
    if request.method == 'POST':
        msg = Message("Запрос с magnavis.ru", recipients=mails)
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
    if request.MOBILE:
        return render_template('mobile/about.html', numbers=numbers, titles=titles)
    else:
        return render_template('about.html', numbers=numbers, titles=titles)


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
