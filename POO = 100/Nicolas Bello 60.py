import requests
import pytest
import time

BASE_URL = "http://127.0.0.1:8000"

@pytest.fixture(scope="module", autouse=True)
def run_api_server():
    print(f"\nPor favor, asegúrate de que la API de FastAPI esté corriendo en {BASE_URL} antes de ejecutar las pruebas.")
    print("Ejecuta 'uvicorn api_to_test:app --reload' en otra terminal.")
    time.sleep(2)
    yield
    print("\nAPI tests finished.")

def test_read_root(run_api_server):
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API!"}

def test_create_item_success(run_api_server):
    item_data = {"name": "Laptop", "price": 1200.0, "is_offer": True}
    response = requests.post(f"{BASE_URL}/items/", json=item_data)
    assert response.status_code == 200
    assert response.json() == item_data

def test_create_item_already_exists(run_api_server):
    item_data = {"name": "Laptop", "price": 1200.0, "is_offer": True}
    response = requests.post(f"{BASE_URL}/items/", json=item_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Item already exists"}

def test_read_non_existent_item(run_api_server):
    response = requests.get(f"{BASE_URL}/items/NonExistentItem")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
