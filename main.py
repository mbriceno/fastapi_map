from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.migrations.initial_migration import initial_migration
from app.seed.initial_seed import initial_seeding
from app.api.v1 import category, location, location_category_reviewed
from app.config.database import Base, engine
from config.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Initializes the database tables when the application starts up.
    """
    initial_migration()
    initial_seeding()
    yield
    Base.metadata.drop_all(bind=engine)

app = FastAPI(
    debug=True,
    title=settings.app_name,
    description=settings.app_description,
    version="1.0.0",
    contact={
        "name": "Miguel Briceño",
        "url": "https://www.linkedin.com/in/miguel-briceno-ve/",
    },
    license={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    },
    lifespan=lifespan
)

app.include_router(category.router, prefix="/api/v1")
app.include_router(location.router, prefix="/api/v1")
app.include_router(location_category_reviewed.router, prefix="/api/v1")
