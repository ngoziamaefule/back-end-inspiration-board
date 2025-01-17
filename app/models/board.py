from sqlalchemy.orm import backref
from app import db

class Board (db.Model):
    board_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)
    cards = db.relationship("Card", back_populates="board")

    def update_attributes(self, request_body):
        self.title = request_body["title"]
        self.owner=request_body["owner"]

    def board_details(self):
        return {
            "board_id": self.board_id,
            "title": self.title,
            "owner": self.owner
        }