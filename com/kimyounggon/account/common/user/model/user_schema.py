from pydantic import BaseModel, EmailStr

# ✅ 기본 스키마 (공통 속성)
class MemberBase(BaseModel):
    user_id: str
    email: EmailStr
    name: str

# ✅ 회원 가입 요청 스키마 (비밀번호 포함)
class MemberCreate(MemberBase):
    password: str 

# ✅ 회원 응답 스키마 (비밀번호 제외)
class MemberResponse(MemberBase):
    class Config:
        from_attributes = True  # SQLAlchemy 모델과 호환 가능
