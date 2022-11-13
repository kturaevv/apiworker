""" 
    Connection might be initialized in many places: tests, sample runs, application itself etc. Interaction 
    with DB takes a lot of repetitive code, thus, ConnManager was moved to separate Singleton Entitity, 
    so no matter where connection is inited the connection will be the same. 
"""

from sqlalchemy.orm import declarative_base, close_all_sessions, sessionmaker
from sqlalchemy import create_engine

from config import get_settings

settings = get_settings()


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ConnManager(metaclass=SingletonMeta):
    
    def __init__(self, echo=False) -> None:
        self.conn_url = "postgresql://{username}:{password}@{host}:5435/{database}".format(
            username = settings.username,
            password = settings.password,
            host = settings.host,
            database = settings.database
        )
        self.engine = create_engine(self.conn_url, echo=echo)
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)()
        self.Base = declarative_base(bind=self.engine)

    def define_tables(self):
        self.Base.metadata.create_all()
    
    def drop_tables(self):
        close_all_sessions()
        self.Base.metadata.drop_all()

    def close_sessions(self):
        close_all_sessions()