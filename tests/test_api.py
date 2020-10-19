from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_get_index():
    response = client.get('/')
    assert response.status_code == 200


def test_post_calculate_with_discount_without_count():
    response = client.post('/with_discount', json={'price': 125})
    assert response.status_code == 422
    assert isinstance(response.json(), dict)

    detail = response.json().get('detail', [])
    assert detail
    assert isinstance(detail[0], dict)

    loc = detail[0].get('loc')
    assert loc
    assert isinstance(loc, list)
    assert loc[1] == 'count'

    msg = detail[0].get('msg')
    assert msg
    assert msg == 'field required'


def test_post_calculate_with_discount_without_price():
    response = client.post('/with_discount', json={'count': 89})
    assert response.status_code == 422
    assert isinstance(response.json(), dict)

    detail = response.json().get('detail', [])
    assert detail
    assert isinstance(detail[0], dict)

    loc = detail[0].get('loc')
    assert loc
    assert isinstance(loc, list)
    assert loc[1] == 'price'

    msg = detail[0].get('msg')
    assert msg
    assert msg == 'field required'


def test_post_calculate_with_discount():
    response = client.post('/with_discount', json={'count': 8, 'price': 125})
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

    result_cost = response.json().get('result_cost')
    assert result_cost


def test_post_calculate_with_tax_without_price():
    response = client.post('/with_tax', json={'state': 'UT'})
    assert response.status_code == 422
    assert isinstance(response.json(), dict)

    detail = response.json().get('detail', [])
    assert detail
    assert isinstance(detail[0], dict)

    loc = detail[0].get('loc')
    assert loc
    assert isinstance(loc, list)
    assert loc[1] == 'price'

    msg = detail[0].get('msg')
    assert msg
    assert msg == 'field required'


def test_post_calculate_with_tax_without_state():
    response = client.post('/with_tax', json={'price': 1204})
    assert response.status_code == 422
    assert isinstance(response.json(), dict)

    detail = response.json().get('detail', [])
    assert detail
    assert isinstance(detail[0], dict)

    loc = detail[0].get('loc')
    assert loc
    assert isinstance(loc, list)
    assert loc[1] == 'state'

    msg = detail[0].get('msg')
    assert msg
    assert msg == 'field required'


def test_post_calculate_with_tax_with_wrong_state():
    response = client.post('/with_tax', json={'price': 125, 'state': 'wrong_state'})
    assert response.status_code == 422
    assert isinstance(response.json(), dict)

    detail = response.json().get('detail', [])
    assert detail
    assert isinstance(detail[0], dict)

    loc = detail[0].get('loc')
    assert loc
    assert isinstance(loc, list)
    assert loc[1] == 'state'

    msg = detail[0].get('msg')
    assert msg
    assert 'unexpected value' in msg


def test_post_calculate_with_tax():
    states = ['UT', 'NV', 'TX', 'AL', 'CA']

    for state in states:
        response = client.post('/with_tax', json={'price': 125, 'state': state})
        assert response.status_code == 200
        assert isinstance(response.json(), dict)

        result_cost = response.json().get('result_cost')
        assert result_cost
