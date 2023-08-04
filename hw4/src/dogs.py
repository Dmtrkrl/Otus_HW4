import requests


BASE_URL = "https://dog.ceo/api"
class DogAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_all_breeds(self):
        return self.make_request('breeds/list/all')

    def get_random_image_by_breed(self):
        return self.make_request('breeds/image/random')

    def get_sub_breeds(self, breed):
        return self.make_request(f'breed/{breed}/list')

    def get_random_image_by_sub_breed(self, breed, sub_breed):
        return self.make_request(f'breed/{breed}/{sub_breed}/images/random')

    def get_multiple_random_images(self, breed, sub_breed, count):
        return self.make_request(f'breed/{breed}/{sub_breed}/images/random/{count}')
