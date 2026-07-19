from httpx import ASGITransport, AsyncClient
from fastapi.testclient import TestClient
import pytest
import pytest_asyncio
from src.database.connection import get_async_db
from src.api.main import app
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)
from sqlalchemy import NullPool, text
from unittest.mock import AsyncMock

from src.dependencies import get_cache_service
from src.services.cache_service import CacheService

from src.tests.config import ASYNC_TEST_DATABASE_URL

test_engine = create_async_engine(
    ASYNC_TEST_DATABASE_URL,
    poolclass=NullPool,
)

TestSessionLocal = async_sessionmaker(
    bind=test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


@pytest_asyncio.fixture
async def db_session():
    connection = await test_engine.connect()
    transaction = await connection.begin()

    session = AsyncSession(bind=connection, expire_on_commit=False)

    async def override_get_async_db():
        yield session

    app.dependency_overrides[get_async_db] = override_get_async_db

    try:
        yield session
    finally:
        app.dependency_overrides.pop(get_async_db, None)

        await transaction.rollback()
        await session.close()
        await connection.close()


@pytest.fixture(autouse=True)
def override_cache_service():
    cache = AsyncMock(spec=CacheService)

    cache.get.return_value = None
    cache.set.return_value = True
    cache.delete.return_value = 1
    cache.delete_pattern.return_value = None

    async def override():
        return cache

    app.dependency_overrides[get_cache_service] = override

    yield

    app.dependency_overrides.pop(get_cache_service, None)


@pytest.fixture()
def client():
    return TestClient(app)


@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as async_client:
        yield async_client


@pytest.fixture(autouse=True)
def clear_dependency_overrides():
    yield
    app.dependency_overrides.clear()


@pytest_asyncio.fixture(autouse=True)
async def clear_database():
    async with test_engine.begin() as conn:
        await conn.execute(text("""
                TRUNCATE TABLE
                    orders,
                    products,
                    users
                RESTART IDENTITY CASCADE;
            """))

    yield
