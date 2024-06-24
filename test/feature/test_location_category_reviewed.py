from test.test_config import client


def test_it_can_get_all_successfully():
    response = client.get("/api/v1/reviews/")
    rjson = response.json()
    first_suggest = {
        "visit": 0,
        "last_visit": None,
        "id": 1,
        "category": {
            "name": "Restaurantes",
            "description": "-----*****-----",
            "id": 1
        },
        "location": {
            "name": "Coma y Beba",
            "latitude": 7.8877313428941145,
            "longitude": -72.49957719536566,
            "id": 1
        },
        "user": {
            "name": "Miguel Briceño",
            "email": "mbriceno-2024@gmail.com",
            "id": 1
        }
    }

    assert response.status_code == 200
    assert rjson[0] == first_suggest


def test_it_can_get_suggested_successfully():
    response = client.get("/api/v1/reviews/suggested", params={"user_id": 1})
    rjson = response.json()

    assert response.status_code == 200
    assert len(rjson) == 10
