from sqlalchemy import ForeignKey
from my_app import db

class Product():
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float)
    category_id = db.Column(db.Integer, ForeignKey('category.id'))
    categories = db.relationship('Category', backref=db.backref('products', lazy='dynamic'))

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return '<Product %d.>' % self.id



class Category():
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %d.>' % self.id