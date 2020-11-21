from sqlalchemy import create_engine, Column, Integer, String, DateTime, \
    ForeignKey, event
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:@localhost:3306/whoscored_db', echo=False, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


def init_db():
    Model.metadata.create_all(bind=engine)


Model = declarative_base(name='Model')
