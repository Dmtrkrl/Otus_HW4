import requests

BASE_URL = 'https://api.openbrewerydb.org/v1'


class OpenBreweryAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, endpoint, params=None):
        url = f'{self.base_url}/{endpoint}'
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_all_breweries(self):
        return self.make_request('breweries')

    def filter_breweries_by_city(self, city):
        params = {'by_city': city}
        return self.make_request('breweries', params=params)

    def get_brewery_by_id(self, brewery_id):
        return self.make_request(f'breweries/{brewery_id}')

    def filter_breweries_by_type(self, brewery_type):
        params = {'by_type': brewery_type}
        return self.make_request('breweries', params=params)

    def get_all_cities(self):
        breweries = self.get_all_breweries()
        cities = {brewery['city'] for brewery in breweries}
        return cities
