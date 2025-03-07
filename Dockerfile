# 1️⃣ Python 3.12.7 환경 설정
FROM python:3.12.7-slim

# 2️⃣ 필수 패키지 설치 (libpq-dev 제거 가능)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 3️⃣ 작업 디렉토리 설정
WORKDIR /app

# 4️⃣ pip 최신 버전 업데이트
RUN pip install --upgrade pip

# 5️⃣ requirements.txt 복사
COPY requirements.txt .

# 6️⃣ 패키지 설치 (asyncpg만 설치됨)
RUN pip install --no-cache-dir -r requirements.txt

# 7️⃣ 애플리케이션 코드 복사
COPY . /app/

# 8️⃣ FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
