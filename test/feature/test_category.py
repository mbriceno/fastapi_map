from test.test_config import client


def test_it_can_get_all_categories_successfully():
    response = client.get("/api/v1/categories/")
    rjson = response.json()
    first_category = {
        "name": "Restaurantes",
        "description": "-----*****-----",
        "id": 1
    }

    assert response.status_code == 200
    assert rjson[0] == first_category
    assert len(rjson) == 4


def test_it_can_create_category_successfully():
    data = {
        "name": "Compras",
        "description": "Locales para comprar",
    }

    response = client.post(
        "/api/v1/categories",
        json=data,
        headers={
            'Content-Type': 'application/json'
        },
    )

    rjson = response.json()

    assert response.status_code == 201
    assert rjson['name'] == "Compras"
    assert rjson['description'] == "Locales para comprar"
