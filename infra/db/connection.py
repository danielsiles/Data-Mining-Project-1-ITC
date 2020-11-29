from abc import ABC, abstractmethod

from sqlalchemy import create_engine, Column, Integer, String, DateTime, \
    ForeignKey, event
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation
from sqlalchemy.ext.declarative import declarative_base

from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

Model = declarative_base(name='Model')


class DBConnection:
    _db_session = None

    @staticmethod
    def get_db_session():
        """
        Returns the db session if exists, otherwise creates one and return it
        :return:
        """
        if DBConnection._db_session is None:
            DBConnection._init_db()
        return DBConnection._db_session

    @staticmethod
    def _init_db():
        """
        Initialize the db session and engine
        """
        engine = create_engine(f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}', echo=False,
                               convert_unicode=True)
        DBConnection._db_session = scoped_session(sessionmaker(autocommit=False,
                                                               autoflush=False,
                                                               bind=engine))
        Model.metadata.create_all(bind=engine)
