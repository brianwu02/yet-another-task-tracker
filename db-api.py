from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, mapper, scoped_session, sessionmaker
from datetime import datetime, date


engine = create_engine('postgresql+psycopg2://test:password@localhost/test-db', convert_unicode=True, echo=False)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
