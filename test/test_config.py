from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.migrations.initial_migration import initial_migration
from app.seed.initial_seed import initial_seeding
from app.config.database import sess_db
from main import app
from config.settings import settings


DB_URL = "postgresql://{}:{}@{}:{}/{}".format(
    settings.db_user,
    settings.db_password,
    settings.db_host,
    settings.db_port,
    settings.db_name
)

engine = create_engine(DB_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

initial_migration(engine)
initial_seeding(engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[sess_db] = override_get_db
client = TestClient(app)
