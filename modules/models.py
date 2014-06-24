from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime, date

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    note = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    def __init__(self, note=None, timestamp=None):
        self.note = note
        self.timestamp = timestamp

    def __repr__(self):
        return "<Note(id='%s', note='%s', timestamp='%s')>" % (
                self.id, self.note, self.timestamp) 
