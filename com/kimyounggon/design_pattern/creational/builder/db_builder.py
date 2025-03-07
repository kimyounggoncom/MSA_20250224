
# ✅ 1. DatabaseBuilder: SQLAlchemy 엔진 및 세션 빌더

from sqlalchemy import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class DatabaseConfigBuilder:
    def __init__(self):
        self._database_url = None
        self._echo = False
        self._future = True
        self._autocommit = False
        self._autoflush = False
        self._engine = None
        self._session_local = None
        self._base = None
    
    def set_database_url(self, database_url: str):
        self._database_url = database_url
        return self
    
    def set_echo(self, echo: bool):
        self._echo = echo
        return self
    
    def set_future(self, future: bool):
        self._future = future
        return self
    
    def set_autocommit(self, autocommit: bool):
        self._autocommit = autocommit
        return self
    
    def set_autoflush(self, autoflush: bool):
        self._autoflush = autoflush
        return self
    
    def build(self):
        if not self._database_url:
            raise ValueError("Database URL must be set.")
        
        self._engine = create_async_engine(
            self._database_url, echo=self._echo, future=self._future
        )
        self._session_local = sessionmaker(
            autocommit=self._autocommit, autoflush=self._autoflush, bind=self._engine
        )
        self._base = declarative_base()
        
        return DatabaseConfig(
            engine=self._engine,
            session_local=self._session_local,
            base=self._base
        )

class DatabaseConfig:
    def __init__(self, engine, session_local, base):
        self.engine = engine
        self.session_local = session_local
        self.base = base
    
    def get_session(self):
        return self.session_local()

# Usage Example
if __name__ == "__main__":
    db_config = (
        DatabaseConfigBuilder()
        .set_database_url("sqlite:///./test.db")
        .set_echo(True)
        .set_future(True)
        .set_autocommit(False)
        .set_autoflush(False)
        .build()
    )
    
    print("Database Engine:", db_config.engine)
    print("Session Local:", db_config.session_local)
    print("Base Model:", db_config.base)
