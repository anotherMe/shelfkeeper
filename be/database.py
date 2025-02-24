from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = "postgresql+psycopg://bernie:l0max@localhost:5432/mystuffdb"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to provide a session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
