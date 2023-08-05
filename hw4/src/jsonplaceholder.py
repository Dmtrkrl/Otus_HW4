import requests

# Пример базового URL для API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Класс для работы с API
class JsonPlaceholderAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, method, endpoint, params=None, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, params=params, json=data)
        response.raise_for_status()
        return response

    def get_post_by_id(self, post_id):
        response = self.make_request("GET", f"posts/{post_id}")
        return response.json()

    def create_new_post(self, post_data):
        response = self.make_request("POST", "posts", data=post_data)
        return response

    def update_post(self, post_id, updated_data):
        response = self.make_request("PUT", f"posts/{post_id}", data=updated_data)
        return response

    def delete_post(self, post_id):
        response = self.make_request("DELETE", f"posts/{post_id}")
        return response

    def get_comments_for_post(self, post_id):
        params = {"postId": post_id}
        response = self.make_request("GET", "comments", params=params)
        return response.json()
