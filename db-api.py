from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, mapper, scoped_session, sessionmaker
from datetime import datetime, date


engine = create_engine('postgresql+psycopg2://test:password@localhost/testdb', convert_unicode=True, echo=False)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()

def init_db():
    metadata.create_all(bind=engine)

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    data = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Note(id='%s', data='%s', timestamp='%s')>" % (
                self.id, self.data, self.timestamp)

# not needed.
#
#note = Table('note', metadata,
#        Column('id', Integer, primary_key=True),
#        Column('note', Text, nullable=False),
#        Column('timestamp', DateTime, nullable=False)
#        )
#
#mapper(Note, note)
