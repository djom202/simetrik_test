import requests


def test_get_response_json():
    url = 'https://jsonplaceholder.typicode.com/todos/1'

    resp = requests.request('GET', url)

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['userId'] == 1
    assert resp_body['id'] == 1
    assert resp_body['title'] == 'delectus aut autem'
    assert resp_body['completed'] == False

    # print response full body as text
    print(resp.text)