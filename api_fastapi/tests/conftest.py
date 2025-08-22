import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from unittest.mock import patch

from app.main import app
from app.database.database import Base, get_db

# --- Pengaturan Database Test (menggunakan SQLite in-memory) ---
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture untuk membuat tabel sebelum test berjalan dan menghapusnya setelah selesai
@pytest.fixture(scope="function", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# --- Override Dependency get_db ---
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# --- Mocking Firebase Auth ---
MOCK_DECODED_TOKEN = {
    "uid": "test_user_uid_123",
    "email": "test@example.com",
    "name": "Test User"
}

@pytest.fixture(scope="module")
def mock_firebase_auth():
    with patch("firebase_admin.auth.verify_id_token") as mock_verify:
        mock_verify.return_value = MOCK_DECODED_TOKEN
        yield mock_verify

# --- Fixture untuk Test Client ---
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c