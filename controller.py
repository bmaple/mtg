from flask import Flask, render_template, send_from_directory
from flask.ext.bootstrap import Bootstrap
from models import *
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    card = Cards.query.first() 
    return card.Nname
    #return render_template('test.html')



if __name__ == '__main__':
    app.run(debug = True)



