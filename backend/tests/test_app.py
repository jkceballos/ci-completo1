from app import app

def test_status():
    client = app.test_client()
    resp = client.get('/status')
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "OK"}
