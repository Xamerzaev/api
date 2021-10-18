from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from mans import db


class Shop(db.Model):
    __tablename__ = "shops"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    texts = db.relationship("Text", backref="shop", lazy=True)
    def add_text(self, name):
        t = Text(name=name, shop_id=self.id)
        db.session.add(t)
        db.session.commit()


class Text(db.Model):
    __tablename__ = "texts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey("shops.id"), nullable=False)