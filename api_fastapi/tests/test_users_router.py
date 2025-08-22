from fastapi.testclient import TestClient
from .conftest import MOCK_DECODED_TOKEN

def test_get_user_me_unauthorized(client: TestClient):
    """
    SKENARIO 1: GAGAL
    Mencoba mengakses endpoint /me tanpa mengirimkan token.
    Harapan: API akan mengembalikan error 401 Unauthorized.
    """
    response = client.get("/api/v1/users/me")
    assert response.status_code == 401
    assert "Not authenticated" in response.json()["detail"]

def test_get_user_me_authorized_creates_new_user(client: TestClient, mock_firebase_auth):
    """
    SKENARIO 2: BERHASIL
    Mengakses endpoint /me dengan token (yang sudah kita 'palsukan').
    Harapan: API akan memverifikasi token, membuat user baru di database test,
             dan mengembalikan data user tersebut.
    """
    # Header "Authorization" ini akan ditangkap oleh `oauth2_scheme` di `auth.py`
    response = client.get(
        "/api/v1/users/me",
        headers={"Authorization": "Bearer fake-token-yang-akan-dimock"}
    )
    
    # Periksa apakah responsnya sukses
    assert response.status_code == 200
    
    # Periksa apakah data yang dikembalikan sesuai dengan data dari token palsu kita
    data = response.json()
    assert data["uid"] == MOCK_DECODED_TOKEN["uid"]
    assert data["email"] == MOCK_DECODED_TOKEN["email"]
    assert data["name"] == MOCK_DECODED_TOKEN["name"]
    assert data["is_premium"] is False # Default value