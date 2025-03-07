from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# ✅ 비동기 PostgreSQL 드라이버(`asyncpg`) 추가
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://myuser:mypassword@database:5432/mydatabase")

# ✅ SQLAlchemy 비동기 엔진 생성
engine = create_async_engine(DATABASE_URL, echo=True)

# ✅ 비동기 세션 팩토리 생성
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, autoflush=False, autocommit=False)

# ✅ SQLAlchemy Base 선언
Base = declarative_base()

# ✅ 비동기 get_db 함수 수정
async def get_db():
    async with SessionLocal() as session:
        yield session
