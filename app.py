from flask import Flask, render_template
from flask_mail import Mail, Message

application = Flask(__name__)
application.config['MAIL_SERVER'] = 'smtp.googlemail.com'
application.config['MAIL_PORT'] = 587
application.config['MAIL_USE_TLS'] = True
application.config['MAIL_USERNAME'] = 'magnavis.site@gmail.com'
application.config['MAIL_DEFAULT_SENDER'] = 'magnavis.site@gmail.com'
application.config['MAIL_PASSWORD'] = '3zT-vZi-qvT-DyR'

@application.route('/')
def home():
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
