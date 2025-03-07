import os
from database import get_db
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from com.kimyounggon.delivery.web.delivery_router import router as delivery_router
from com.kimyounggon.design_pattern.creational.singleton.db_singleton import db_singleton
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

#docker ps 
#docker ps -a
#docker images
#docker start backend 
#docker start database
#docker compose up
#docker exec -it backend bash  백엔드 컨테이너 내부로 들어가기 
#docker exec -it database psql -U myuser -d mydatabase 컨테이너 내부에서 PostgreSQL 실행
#docker compose logs backend 도커 컴포즈에서 도커 안을 바라보는거 
#python -m uvicorn main:app --reload
#docker docker compose build --no-cache
#docker 

app = FastAPI()



print("🎋🎄🎍",db_singleton.db_hostname)
print("🎋🎄🎍",db_singleton.db_username)
print("🎋🎄🎍",db_singleton.db_password)
print("🎋🎄🎍",db_singleton.db_port)
print("🎋🎄🎍",db_singleton.db_database)
print("🎋🎄🎍",db_singleton.db_charset)


app.include_router(delivery_router, prefix="/delivery", tags=["Delivery"])

@app.get("/")
async def home():
    return HTMLResponse(content=f"""
<body>
<div style="width: 400px; margin: 50 auto;">
    <h1> 현재 서버 구동 중입니다.</h1>
</div>
</body>
""")

# @app.get("/users")
# async def get_users():
#     print("🐻🤦‍♀️❤️✍️🤔get_users 로 진입함")
#     query = "SELECT * FROM member"

@app.get("/users")
async def get_users(db: AsyncSession = Depends(get_db)):
    print("🐻🤦‍♀️❤️✍️🤔 get_users 로 진입함")

    # ✅ SQL 실행 (text()로 감싸기)
    query = text("SELECT * FROM member")  # 여기서 text()로 감싸줌
    result = await db.execute(query)
    rows = result.fetchall()  # 결과 가져오기

    # ✅ JSON 응답 반환
    return JSONResponse(content={"users": [dict(row._mapping) for row in rows]})  # ✅ _mapping 사용


    
  


# @app.get("/")
# def read_root():
#     return {"message": "FastAPI + PostgreSQL 연동 성공!"}

# @app.get("/")
# async def get_users():
#     query = "SELECT * FROM users"
#     result = await async_database.fetch(query)
#     return {"users": [dict(row) for row in result]}
# @app.on_event("shutdown")
# async def shutdown():
#     await async_database.close()

