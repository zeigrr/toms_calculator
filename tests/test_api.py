from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_get_index():
    response = client.get('/')
    assert response.status_code == 200


def test_post_calculate_without_count():
    response = client.post('/', json={'price': 125, 'state': 'UT'})
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


def test_post_calculate_without_price():
    response = client.post('/', json={'count': 5, 'state': 'UT'})
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


def test_post_calculate_without_state():
    response = client.post('/', json={'count': 5, 'price': 125})
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


def test_post_calculate_with_wrong_state():
    response = client.post('/', json={'count': 5, 'price': 125, 'state': 'wrong_state'})
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


def test_post_calculate_with_count_less_than_zero():
    response = client.post('/', json={'count': -1, 'price': 125, 'state': 'UT'})
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
    assert msg == 'count must be greater than zero'


def test_post_calculate_with_price_less_than_zero():
    response = client.post('/', json={'count': 5, 'price': -1, 'state': 'UT'})
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
    assert msg == 'price must be greater than zero'


def test_post_calculate():
    response = client.post('/', json={'count': 5, 'price': 125, 'state': 'UT'})
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

    cost_with_discount = response.json().get('cost_with_discount')
    assert cost_with_discount

    cost_with_tax = response.json().get('cost_with_tax')
    assert cost_with_tax
