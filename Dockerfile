# 1️⃣ FastAPI를 실행할 Python 베이스 이미지 설정
FROM python:3.12.7-slim

# 2️⃣ 작업 디렉토리 설정
WORKDIR /com

# 3️⃣ 필요한 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4️⃣ 애플리케이션 코드 복사
COPY . .

# 5️⃣ FastAPI 실행 (포트 8000)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
