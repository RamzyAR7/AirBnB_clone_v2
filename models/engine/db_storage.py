#!/usr/bin/python3
"""New engine DBStorage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State, Base


class DBStorage:
    """DataBase storage type"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:\
                                      {}@{}/{}'.format(
        getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
        getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
        pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        dic = {}
        classes = [State, City, Review, Amenity, Place, User]
        if cls is None:
            for clas in classes:
                querying = self.__session.query(clas)
                for obj in querying:
                    dic[f"{clas}.{obj.id}"] = obj
        elif cls in classes:
            querying = self.__session.query(cls)
            for obj in querying:
                dic[f"{clas}.{obj.id}"] = obj
        return dic

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.query(eval(type(obj).__name__)).filter_by(
                eval(type(obj).__name__).id==obj.id).delete()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        presession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(presession)
        self.__session = session()
