from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime, date 

from flask import jsonify

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    note = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    def as_dict(self):
        """return as dictionary"""
        return {
                'id': self.id,
                'note': self.note,
                'timestamp': self.timestamp
                }

    @classmethod
    def jsonify_all(cls):
        """Returns all Note instances as JSON Flask response"""
        return jsonify(notes=[note.as_dict() for note in cls.query.all()])

    def __init__(self, note=None, timestamp=None):
        self.note = note
        self.timestamp = timestamp

    def __repr__(self):
        return "<Note(id='%s', note='%s', timestamp='%s')>" % (
                self.id, self.note, self.timestamp)

