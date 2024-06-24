from test.test_config import client


def test_it_can_get_all_locations_successfully():
    response = client.get("/api/v1/locations/")
    rjson = response.json()
    first_location = {
        "name": "Coma y Beba",
        "latitude": 7.8877313428941145,
        "longitude": -72.49957719536566,
        "id": 1
    }

    assert response.status_code == 200
    assert rjson[0] == first_location
    assert len(rjson) == 16


def test_it_can_create_location_successfully():
    data = {
        "name": "Lago Dumar",
        "latitude": 7.866558544842614,
        "longitude": -72.60971962480196
    }

    response = client.post(
        "/api/v1/locations",
        json=data,
        headers={
            'Content-Type': 'application/json'
        },
    )

    rjson = response.json()

    assert response.status_code == 201
    assert rjson['name'] == "Lago Dumar"
    assert rjson['latitude'] == 7.866558544842614
    assert rjson['longitude'] == -72.60971962480196
    assert 'id' in rjson
