# tests/test_routes.py
def test_read_product_route(client):
    response = client.get('/api/products/1')
    assert response.status_code == 200
# tests/test_routes.py
def test_update_product_route(client):
    response = client.put('/api/products/1', json={
        'name': 'Updated Product',
        'category': 'Category1',
        'availability': True
    })
    assert response.status_code == 200
# tests/test_routes.py
def test_delete_product_route(client):
    response = client.delete('/api/products/1')
    assert response.status_code == 204
# tests/test_routes.py
def test_list_all_products_route(client):
    response = client.get('/api/products')
    assert response.status_code == 200
    assert len(response.json()) > 0

