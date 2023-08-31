from flask import Flask, render_template

application = Flask(__name__)


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
