""" 
    Connection might be initialized in many places: tests, sample runs, application itself etc. Interaction 
    with DB takes a lot of repetitive code, thus, ConnManager was moved to separate Singleton Entitity, 
    so no matter where connection is inited the connection will be the same. 
"""

from sqlalchemy.orm import declarative_base, close_all_sessions, sessionmaker, DeclarativeMeta
from sqlalchemy import create_engine

from . import config

settings = config.get_settings()


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
    
    def __init__(self, echo=False, test=False) -> None:
        print("Initializing database connection...")
        if test == False and settings.host != 'localhost':
            raise ValueError("Trying to connect to remote DB instance for test. Connect locally instead.")

        self.conn_url = "postgresql://{username}:{password}@{host}:5435/{database}".format(
            username = settings.username,
            password = settings.password,
            host = settings.host,
            database = settings.database
        )
        self.engine = create_engine(self.conn_url, echo=echo)
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)()
        self.test_schema = 'test'
        if test == True:
            from sqlalchemy.schema import CreateSchema
            if not self.engine.dialect.has_schema(self.engine, self.test_schema):
                self.engine.execute(CreateSchema(self.test_schema))
            self.Base = declarative_base(bind=self.engine)
            self.Base.metadata.schema = self.test_schema
        else:
            self.Base = declarative_base(bind=self.engine)

    def define_tables(self):
        self.Base.metadata.create_all()
    
    def drop_tables(self):
        close_all_sessions()
        self.Base.metadata.drop_all()

    def close_sessions(self):
        close_all_sessions()


class TestPrefixerMeta(DeclarativeMeta):
    """ 
        Quick hack to separate test and prod databases without schema usage.
        When used, appends <test_> prefix to each table and foreign key constraint.
        Does not apply to Table(...) M2M junction table objects.
        TODO finish later
    """
    def __init__(cls, name, bases, dict_):
        if '__tablename__' in dict_:

            from sqlalchemy.sql.schema import ForeignKeyConstraint, ForeignKey, Column
            cls.__tablename__ = dict_['__tablename__'] = \
                'test_' + dict_['__tablename__']

            for i in cls.__dict__.values():
                if type(i) == Column and i.foreign_keys:
                    fk = i.foreign_keys.pop()
                    fk._colspec = 'test_' + fk._colspec
        return super().__init__(name, bases, dict_)

conn = ConnManager()
Base = conn.Base