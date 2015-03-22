from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
import Secret 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Secret.DB_URI
db = SQLAlchemy(app)

class Cards(db.Model):
    __tablename__ = "Ncards"
    Nid = db.Column(db.Integer, primary_key = True)
    Nname = db.Column(db.Text)

    def __repr__(self):
        return '<Cards %r>' % self.Nname
#need to fix
class Sets(db.Model):
    __tablename__ = "Nsets"
    Nid = db.Column(db.Integer, primary_key = True)
    Nname = db.Column(db.Text)

    def __repr__(self):
        return '<Sets %r>' % self.Nname
