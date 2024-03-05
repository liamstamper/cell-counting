# tests/test_views.py
def test_home_page(client):
    """Test the home page is accessible."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data

# Add other view function tests here
