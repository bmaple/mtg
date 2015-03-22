from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
import Secret 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Secret.DB_URI
db = SQLAlchemy(app)




decksass = db.Table('DECKCARDS',
        db.Column('deck_id', db.Integer, db.ForeignKey('decks.id')),
        db.Column('card_id', db.Integer, db.ForeignKey('cards.Nid'))
)
class Cards(db.Model):
    __tablename__ = "Ncards"
    Nid = db.Column(db.Integer, primary_key = True)
    Nname = db.Column(db.Text)
    def __repr__(self):
        return '<Cards %r>' % self.Nname
#deck table for a created deck
class  Deck(db.Model):
    __tablename__ = "DECKS"
    name = db.Column(db.Text, unique=True)
    id = db.Column(db.Integer, primary_key=True)
    decksass = db.relationship('Cards', secondary=decksass,
            backref=db.backref('decks', lazy='dynamic')) # may remove primary join
    def __repr__(self):
        return '<DECKS %r>' % self.name
    """
#storage table for what's in a person's deck
class  DecksCards(db.Model):
    __tablename__ = "DECKCARDS"
    deck_id = db.Column(db.Integer)
    card_id = db.Column(db.Integer)
    def __repr__(self):
        return '<DECKCARDS %r>' % self.deck_id
        """
"""
class Sets(db.Model):
    __tablename__ = "Nsets"
    #Nid = db.Column(db.Integer, primary_key = True)
    #Nname = db.Column(db.Text)
    def __repr__(self):
        return '<Sets %r>' % self.Nname
        """

