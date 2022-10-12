from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Card(db.model):
    """card information"""
    __tablename__ = 'cards'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(50)
    )
    suit = db.Column(
        db.String(50)
    )
    value = db.Column(
        db.String(50)
    )
    type = db.Column(
        db.String(50)
    )
    business_and_career = db.Column(
        db.String
    )
    family_and_relationships = db.Column(
        db.String
    )
    health_and_wellbeing = db.Column(
        db.String
    )
    journal_prompts = db.Column(
        db.String
    )
    card_image = db.Column(
        db.String
    )

class Deck(db.model):
    """deck information"""

    __tablename__ = 'decks'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )


def connect_db(app):
    db.app = app
    db.init_app(app)
