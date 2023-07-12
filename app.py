from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', title='Home')


@app.route('/about')
def about():
    return render_template('index.html', title='About')


if __name__ == '__main__':
    app.run()
