from dotenv import load_dotenv
import os

load_dotenv(".env.test")

TEST_DATABASE_URL = os.getenv("DATABASE_URL")

if TEST_DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL is not set in .env.test")

ASYNC_TEST_DATABASE_URL = TEST_DATABASE_URL.replace(
    "postgresql://", "postgresql+asyncpg://"
)
