from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, mapper, scoped_session, sessionmaker
from datetime import datetime, date


engine = create_engine('postgresql+psycopg2://test:password@localhost/testdb',
        convert_unicode=True, echo=False)

db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine))

metadata = MetaData()
Base = declarative_base()

def init_db():
    """ import all modules here that might define models so that
    they will be registered properly on the metadata. Otherwise,
    you will have to import them first before calling init_db()
    """
    metadata.create_all(bind=engine)




# not needed.
#
#note = Table('note', metadata,
#        Column('id', Integer, primary_key=True),
#        Column('note', Text, nullable=False),
#        Column('timestamp', DateTime, nullable=False)
#        )
#
#mapper(Note, note)
