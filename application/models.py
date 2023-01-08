import flask
from application import db



class User(db.Document):
    Title    =   db.IntField( unique=True )
    Movies  =   db.StringField( max_length=50 )
    Rating   =   db.StringField( max_length=50 )
    Genre     =   db.StringField( max_length=30 )