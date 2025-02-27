
# from pytz import timezone
# from datetime import datetime
# from typing import Callable
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from com.kimyounggon.auth.admin.web.admin_router import router as admin_router
from com.kimyounggon.auth.user.web.user_router import router as user_router
from com.kimyounggon.delivery.web.delivery_router import router as delivery_router



# python -m uvicorn main:app --reload
# http://127.0.0.1:8000 

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(delivery_router, prefix="/delivery", tags=["Delivery"])
# current_time: Callable[[], str] = lambda: datetime.now(datetime.timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S")

@app.get(path="/")
async def home():
    return HTMLResponse(content=f"""
<body>
<div style="width: 400px; margin: 50 auto;">
    <h1> 현재 서버 구동 중입니다.</h1>
    
</div>
</body>
""")

@app.get("/")
def read_root(): 
    return {"main": "메인 라우터"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
