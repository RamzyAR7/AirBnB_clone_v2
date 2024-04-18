from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models import base_model
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST", default="localhost")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV", default="production")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host,
                                                 db, pool_pre_ping=True))

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        """Query all objects of a particular class."""
        objs = {}
        if cls:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                objs[f"{cls.__name__}.{obj.id}"] = obj
        else:
            for model_class in [State, City]:
                query_result = self.__session.query(model_class).all()
                for obj in query_result:
                    objs[f"{model_class.__name__}.{obj.id}"] = obj
        return objs

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))
