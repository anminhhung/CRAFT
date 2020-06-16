from app import db
from datetime import datetime

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(200), index=True, unique=True) 
    resultPhotos = db.relationship('CraftPhoto', backref='root', lazy='dynamic')
    def __repr__(self):
        return '<Link of Photo: {}>'.format(self.link)

class CraftPhoto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(200), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    photo_id = db.Column(db.Integer, db.ForeignKey('photo.id'))
