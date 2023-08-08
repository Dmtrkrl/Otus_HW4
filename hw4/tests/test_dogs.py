import pytest
from hw4.src.dogs import *


@pytest.fixture
def api():
    return DogAPI(BASE_URL)


def test_get_all_breeds(api):
    response = api.get_all_breeds()
    assert response["status"] == "success"


def test_random_image_by_breed(api):
    response = api.get_random_image_by_breed()
    assert response["status"] == "success"
    assert "message" in response


@pytest.mark.parametrize("breed", ["bulldog", "poodle", "hound"])
def test_sub_breeds(api, breed):
    response = api.get_sub_breeds(breed)
    assert response["status"] == "success"
    assert isinstance(response["message"], list)


@pytest.mark.parametrize("breed, sub_breed", [("hound", "afghan"), ("hound", "basset")])
def test_random_image_by_sub_breed(api, breed, sub_breed):
    response = api.get_random_image_by_sub_breed(breed, sub_breed)
    assert response["status"] == "success"
    assert "message" in response


@pytest.mark.parametrize("breed, sub_breed, count", [("hound", "afghan", 3)])
def test_multiple_random_images(api, breed, sub_breed, count):
    response = api.get_multiple_random_images(breed, sub_breed, count)
    assert response["status"] == "success"
    assert isinstance(response["message"], list)
    assert len(response["message"]) == count
