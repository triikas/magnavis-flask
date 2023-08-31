from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
