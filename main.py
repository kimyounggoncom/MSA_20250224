
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from com.kimyounggon.delivery.web.delivery_router import router as delivery_router
from com.kimyounggon.design_pattern.creational.builder.db_builder import get_db




app = FastAPI()

# print("🎋🎄🎍",db_singleton.db_hostname)
# print("🎋🎄🎍",db_singleton.db_username)
# print("🎋🎄🎍",db_singleton.db_password)
# print("🎋🎄🎍",db_singleton.db_port)
# print("🎋🎄🎍",db_singleton.db_database)
# print("🎋🎄🎍",db_singleton.db_charset)


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

@app.get("/users")
async def get_users(db= Depends(get_db)):
    print("😎😀➕ get/users로 진입")
    query = "SELECT * FROM member"
    try:
        results = await db.fetch(query)
        print("데이터 조회 결과:", results)

        return {"users": [dict(record) for record in results]}
    except Exception as e:
        print(f"⚠️ 데이터베이스 쿼리 실행 중 오류 발생: {str(e)}")
        return {"error": "데이터 조회 중 오류가 발생했습니다"}
    


    




