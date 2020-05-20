from flask import Flask, render_template, request
from prime import primeFactors

app = Flask(__name__)


@app.route('/')
def all():
    return render_template('home.html', title='Home Page')


@app.route('/prime_web', methods=['GET', 'POST'])
def prime_web():
    if request.method == 'POST':
        number = int(request.form.get('number'))
        factor = primeFactors((number))
        return render_template('prime_web.html', title='Prime Factorize', number=number, factor=factor)
    else:
        return render_template('prime_web.html',
                               title='Prime Factorize')


@app.route('/name')
def test():
    return render_template('name.html')


@app.route('/hello_name', methods=['GET', 'POST'])
def hello_name():
    if request.method == 'GET':
        return 'Please fill the form'
    else:
        name = request.form.get("name")
        return render_template('logic.html', name=name)


# Costom 404
@app.route('/<string:error>')
def error(error):
    return f'Oh oh <b>localhost/{error}</b> is not a valid address'


if __name__ == "__main__":
    app.run(debug=True)
