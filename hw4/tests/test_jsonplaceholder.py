import pytest
from hw4.src.jsonplaceholder import *


@pytest.fixture
def api():
    return JsonPlaceholderAPI(BASE_URL)


def test_get_post_by_id(api):
    post_id = 1
    post = api.get_post_by_id(post_id)
    assert post["id"] == post_id


def test_create_new_post(api):
    post_data = {
        "title": "Test Post",
        "body": "This is a test post.",
        "userId": 1
    }
    response = api.create_new_post(post_data)
    assert response.status_code == 201


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_update_post(api, post_id):
    updated_data = {
        "title": "Updated Title",
        "body": "This is the updated body."
    }
    response = api.update_post(post_id, updated_data)
    assert response.status_code == 200


def test_delete_post(api):
    post_id = 1
    response = api.delete_post(post_id)
    assert response.status_code == 200


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_comments_for_post(api, post_id):
    comments = api.get_comments_for_post(post_id)
    assert all(comment["postId"] == post_id for comment in comments)
