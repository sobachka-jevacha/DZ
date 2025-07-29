import requests


key = "EJoAOwIQSwS0nRKg48kiB7o8w9ou7CH1DPEM-ZNOv+fggMmQBaDCqPSbOGRQrg5N"
base_url = "https://ru.yougile.com"


def test_post_positive():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    payload = {
        "title": "Тестовый проект"
    }

    url = f"{base_url}/api-v2/projects"
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 201
    print(response.json())


def test_post_negative():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "
    }

    payload = {
        "title": "Тестовый проект"
    }

    url = f"{base_url}/api-v2/projects"
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 401
    print(response.json())


def test_put_positive():
    project_id = "bb5e49f0-f363-4fb4-910c-8098106a4b80"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    payload = {
        "title": "Тестовый проект"
    }

    url = f"{base_url}/api-v2/projects/{project_id}"
    response = requests.put(url, json=payload, headers=headers)
    assert response.status_code == 200
    print(response.json())


def test_put_positive_negative():
    project_id = "bb5e49f0-f363-4fb4-910c-8098106a4b80"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "123"
    }

    payload = {
        "title": "Тестовый проект"
    }

    url = f"{base_url}/api-v2/projects/{project_id}"
    response = requests.put(url, json=payload, headers=headers)
    assert response.status_code == 401
    print(response.json())


def test_get_positive():
    project_id = "bb5e49f0-f363-4fb4-910c-8098106a4b80"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    url = f"{base_url}/api-v2/projects/{project_id}"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    print(response.json())


def test_get_negative():
    project_id = "bb5e49f0-f363-4fb4-910c-8098106a4b80"

    url = f"{base_url}/api-v2/projects/{project_id}"
    response = requests.get(url)
    assert response.status_code == 401
    print(response.json())