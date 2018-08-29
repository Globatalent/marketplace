from rest_framework import status
from rest_framework.test import APITestCase

from marketplace.users.models import User
from marketplace.users.tests.factories import UserFactory


class VerifyEmailAPITests(APITestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_request_restore_code(self):
        self.user.is_email_verified = False
        self.user.save()
        self.assertFalse(self.user.is_email_verified)
        data = {
            "verification_code": self.user.verification_code,
        }
        response = self.client.post(
            "/api/v1/verify_email/",
            data=data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(pk=self.user.pk)
        self.assertTrue(user.is_email_verified)


class RestorePasswordAPITests(APITestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_request_restore_code(self):
        self.assertIsNone(self.user.restore_password_code)
        data = {
            "email": self.user.email,
        }
        response = self.client.post(
            "/api/v1/request_restore_code/",
            data=data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(pk=self.user.pk)
        self.assertIsNotNone(user.restore_password_code)

    def test_restore_password(self):
        self.user.send_restore_code()
        data = {
            "password": "new_password",
            "repeat_password": "new_password",
            "restore_password_code": self.user.restore_password_code,
        }
        response = self.client.post(
            "/api/v1/restore_password/",
            data=data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(pk=self.user.pk)
        self.assertTrue(user.check_password(data["password"]))
