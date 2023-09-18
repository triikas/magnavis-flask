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
        msg = Message("Запрос с magnavis.ru", recipients=['q1113p@mail.ru'])
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        comment = request.form.get('comment')
        msg.body = "Имя: {}\nПочта: {}\nТелефон: {}\nКомментарий: {}".format(name, email, number, comment)
        mail.send(msg)
        flash("Запрос отправлен")
        return redirect(url_for('home'))
    # if str((request.form.get('name'))) != "None":
    #     flash("Запрос отправлен")

    return render_template('home.html')

@application.route('/contacts')
def contacts():
    return render_template('contacts.html')

@application.route('/payment')
def payment():
    return render_template('payment.html')

@application.route('/services')
def services():
    return render_template('services.html')

@application.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=False)
