from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# ✅ .env 파일 로드
load_dotenv()

# ✅ 환경 변수에서 데이터베이스 연결 정보 가져오기
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://myuser:mypassword@database:5432/mydatabase")

# ✅ SQLAlchemy 비동기 엔진 생성
engine = create_async_engine(DATABASE_URL, echo=True)

# ✅ 비동기 세션 팩토리 생성
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, autoflush=False, autocommit=False)

# ✅ SQLAlchemy Base 선언
Base = declarative_base()

# ✅ 비동기 DB 세션 생성 함수
async def get_db():
    async with SessionLocal() as session:
        yield session  # 비동기 컨텍스트에서 사용
