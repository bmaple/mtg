from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import ForeignKey
import Secret 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Secret.DB_URI
db = SQLAlchemy(app)


class Cards(db.Model):
    __tablename__ = "Ncards"
    Nid = db.Column(db.Integer, primary_key = True)
    Nname = db.Column(db.Text)
    decks = db.relationship('DECKS', secondary='DecksCards')
    def __repr__(self):
        return '<Cards %r>' % self.Nname
#deck table for a created deck
class  Decks(db.Model):
    __tablename__ = "DECKS"
    name = db.Column(db.Text, unique=True)
    id = db.Column(db.Integer, primary_key=True)
    cards = db.relationship(Cards, secondary='DecksCards')
    def __repr__(self):
        return '<DECKS %r>' % self.name

class  DecksCards(db.Model):
    __tablename__ = "DECKCARDS"
    deck_id = db.Column(db.Integer, db.ForeignKey('DECKS.id'), primary_key=True)
    card_id = db.Column(db.Integer, db.ForeignKey('Ncards.Nid'), primary_key=True)
    def __repr__(self):
        return '<DECKCARDS %r>' % self.deck_id



"""
class Sets(db.Model):
    __tablename__ = "Nsets"
    #Nid = db.Column(db.Integer, primary_key = True)
    #Nname = db.Column(db.Text)
    def __repr__(self):
        return '<Sets %r>' % self.Nname
        """

