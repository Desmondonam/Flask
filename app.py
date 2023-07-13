from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


class NameForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def hello():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        return render_template('greeting.html', name=name)
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run()
