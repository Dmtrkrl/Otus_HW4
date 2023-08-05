import pytest
from hw4.src.openbrewerydb import *


@pytest.fixture
def api():
    return OpenBreweryAPI(BASE_URL)


def test_get_all_breweries(api):
    breweries = api.get_all_breweries()
    assert len(breweries) > 0


@pytest.mark.parametrize("city", ["San Diego", "Denver"])
def test_filter_breweries_by_city(api, city):
    breweries = api.filter_breweries_by_city(city)
    for brewery in breweries:
        assert brewery['city'] == city


def test_get_brewery_by_id(api):
    brewery_id = '701239cb-5319-4d2e-92c1-129ab0b3b440'
    brewery = api.get_brewery_by_id(brewery_id)
    assert brewery['id'] == brewery_id


@pytest.mark.parametrize("brewery_type", ["micro", "regional", "brewpub"])
def test_filter_breweries_by_type(api, brewery_type):
    breweries = api.filter_breweries_by_type(brewery_type)
    for brewery in breweries:
        assert brewery['brewery_type'].lower() == brewery_type


def test_get_all_cities(api):
    cities = api.get_all_cities()
    assert len(cities) > 0
