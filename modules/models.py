from sqlalchemy import Column, Integer, String, Text
from module.database import Base

class Note(Base):
    __tablename == 'notes'
    id = Column(Integer, primary_key=True)
    data = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    def __init__(self, data=None, timestamp=None):
        self.data = data 
        self.timestamp = timestamp

    def __repr__(self):
        return "<Note(id='%s', data='%s', timestamp='%s')>" % (
                self.id, self.data, self.timestamp) 
