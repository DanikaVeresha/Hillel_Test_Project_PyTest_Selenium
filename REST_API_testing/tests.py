"""
For https://gorest.co.in/, write test(s) to check post creation.
User, for who post will be created, should be created for test and removed after test
Post format: {'title': '<POST_TITLE>', 'body': '<POST_BODY>'}
You could write it in one file
"""
import requests


class TestCreatePost:

    HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"
    }

    USERDATA = {
        'name': 'John Doe',
        'gender': 'male',
        'email': 'john@ce.com',
        'status': 'active',
    }

    POSTDATA = {
        'title': 'My Post',
        'body': 'This is my first post'
    }

    URL_CREATE_USER = 'https://gorest.co.in/public/v2/users'

    def return_user_id(self):
        response_id = requests.get(
            url=self.URL_CREATE_USER,
            headers=self.HEADERS
        )
        for item in response_id.json():
            if item['name'] == 'John Doe':
                return item['id']

    def return_id_if_user_not_exist(self):
        response_id = requests.get(
            url=self.URL_CREATE_USER,
            headers=self.HEADERS
        )
        for item in response_id.json():
            if item['name'] != 'John Doe':
                return 200

    def test_create_user(self):
        response_user = requests.post(
            url=self.URL_CREATE_USER,
            headers=self.HEADERS,
            json=self.USERDATA
        )
        assert response_user.status_code == 201

    def test_response_status_code_for_request_get_user(self):
        response_code = requests.get(
            url=self.URL_CREATE_USER,
            headers=self.HEADERS
        )
        assert response_code.status_code == 200

    def test_user_data(self):
        response_userdata = requests.get(
            f'{self.URL_CREATE_USER}/{self.return_user_id()}',
            headers=self.HEADERS
        )
        assert response_userdata.json()['name'] == self.USERDATA['name']
        assert response_userdata.json()['email'] == self.USERDATA['email']
        assert response_userdata.json()['gender'] == self.USERDATA['gender']
        assert response_userdata.json()['status'] == self.USERDATA['status']

    def test_create_post(self):
        response_post = requests.post(
            f'{self.URL_CREATE_USER}/{self.return_user_id()}/posts',
            headers=self.HEADERS,
            json=self.POSTDATA
        )
        assert response_post.status_code == 201

    def test_response_status_code_for_request_get_post(self):
        response_code = requests.get(
            f'{self.URL_CREATE_USER}/{self.return_user_id()}/posts',
            headers=self.HEADERS
        )
        assert response_code.status_code == 200

    def test_post_data(self):
        response_postdata = requests.get(
            f'{self.URL_CREATE_USER}/{self.return_user_id()}/posts',
            headers=self.HEADERS
        )
        assert response_postdata.json()[0]['title'] == self.POSTDATA['title']
        assert response_postdata.json()[0]['body'] == self.POSTDATA['body']

    def test_delete_user(self):
        response_delete = requests.delete(
            f'{self.URL_CREATE_USER}/{self.return_user_id()}',
            headers=self.HEADERS
        )
        assert response_delete.status_code == 204

    def test_response_status_code_for_request_get_user_after_user_delete(self):
        response_code = requests.get(
            f'{self.URL_CREATE_USER}/{self.return_id_if_user_not_exist()}',
            headers=self.HEADERS
        )
        assert response_code.status_code == 404

    def test_userdata_after_user_delete(self):
        response_userdata = requests.get(
            f'{self.URL_CREATE_USER}/{self.return_id_if_user_not_exist()}',
            headers=self.HEADERS
        )
        assert response_userdata.json() == {'message': 'Resource not found'}

    def test_response_status_code_for_request_get_post_after_user_delete(self):
        response_code = requests.get(
            f'{self.URL_CREATE_USER}/{self.return_id_if_user_not_exist()}/posts',
            headers=self.HEADERS
        )
        assert response_code.status_code == 200

    def test_postdata_after_user_delete(self):
        response_postdata = requests.get(
            f'{self.URL_CREATE_USER}/{self.return_id_if_user_not_exist()}/posts',
            headers=self.HEADERS
        )
        assert response_postdata.json() == []

