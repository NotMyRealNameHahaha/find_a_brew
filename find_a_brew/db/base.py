from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
