from flask import Flask, render_template, send_from_directory, flash, redirect
from flask.ext.bootstrap import Bootstrap
from models import *
from reg import *
from Secret import *
app = Flask(__name__)
app.secret_key = Secret.key
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    card = Cards.query.first()
    return card.Nname

    #return render_template('test.html')
@app.route('/users', methods =['GET', 'POST'])
def user():
    username = None
    #email = None
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(name = form.username.data)
        form.username.data = ''
        db.session.add(user)
        db.session.commit()
    #    email = form.email.data
    #    form.email.data = ''
        flash('registration accepted')
        #return redirect('/success')
    return render_template('user.html', form=form )
@app.route('/success')
def regSuc():
    firstUser = Users.query.first()
    return firstUser 



if __name__ == '__main__':
    app.run(debug = True)



