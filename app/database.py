from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from dotenv import load_dotenv
from os import getenv


load_dotenv()

#"postgresql+asyncpg://user:password@postgresserver/db"
DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{getenv('POSTGRESQL_USER')}:"
    f"{getenv('POSTGRESQL_PASSWORD')}@"
    f"{getenv('POSTGRESQL_HOST')}:"
    f"{getenv('POSTGRESQL_PORT')}/"
    f"{getenv('POSTGRESQL_DB')}"
)

engine = create_async_engine(DATABASE_URL, echo=True)

async_session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

async def get_session():
    session = async_session_factory()
    try:
        yield session
        await session.commit()
    except:
        await session.rollback()
    finally:
        await session.close()