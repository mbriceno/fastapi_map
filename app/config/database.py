from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import settings

DB_URL = "postgresql://{}:{}@{}:{}/{}".format(
    settings.db_user,
    settings.db_password,
    settings.db_host,
    settings.db_port,
    settings.db_name
)

engine = create_engine(DB_URL)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()
