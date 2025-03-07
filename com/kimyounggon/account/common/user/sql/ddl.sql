CREATE TABLE member (
    user_id VARCHAR(15) PRIMARY KEY,  -- 문자열 타입의 사용자 ID (최대 15자)
    email VARCHAR(20) NOT NULL UNIQUE,  -- 이메일 (중복 방지)
    password VARCHAR(15) NOT NULL,  -- 비밀번호 (최대 15자)
    name VARCHAR(10) NOT NULL  -- 이름 (최대 10자)
);



