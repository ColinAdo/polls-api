from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from rest_framework.authtoken.models import Token

from .models import Poll
from .import views


class TestPoll(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = views.PollViewSet.as_view({'get': 'list'})
        self.url = '/polls/'

        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return  User.objects.create(
            username="TestUser",
            password="TestPassword",
        )

    def test_list(self):
        request = self.factory.get(self.url,
                    HTTP_AUTHORIZATION=f'Token {self.token.key}')
        
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        
    # Using client instance
    def test_list2(self):
        response = self.client.get(
            self.url,
            HTTP_AUTHORIZATION=f'Token {self.token.key}'
            )
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        
    def test_create(self):
        param = {
            "question": "How are you?",
            "created_by": 1
        }
        response = self.client.post(
            self.url,
            param,
            HTTP_AUTHORIZATION=f'Token {self.token.key}'
        )
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))
