from flask import Flask, render_template, send_from_directory
from flask.ext.bootstrap import Bootstrap
from models import *
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    cardInDeck  = Deck.query.join(Cards).first()
    return cardInDeck.Nname
    #return render_template('test.html')
#@app.route('/deck')
#def deckIndex():



if __name__ == '__main__':
    app.run(debug = True)



