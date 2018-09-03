from PIL import Image
from django.core.files.temp import NamedTemporaryFile
from rest_framework import status
from rest_framework.test import APITestCase

from marketplace.athletes.models import Athlete
from marketplace.athletes.tests.factories import AthleteFactory, ReviewFactory
from marketplace.users.models import User
from marketplace.users.tests.factories import UserFactory
from marketplace.supporters.tests.factories import SupporterFactory
from marketplace.supporters.models import Supporter


class AthletesAPITests(APITestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_register_athlete(self):
        users = User.objects.all().count()
        athletes = Athlete.objects.all().count()
        data = {
            "first_name": "foo",
            "last_name": "foo",
            "country": "Spain",
            "date_of_birth": "1985-1-27",
            "sport": "basket",
            "sex": 'MALE',
            "email": "foo@example.com",
            "password": "pass1234",
            "repeat_password": "pass1234",
        }
        response = self.client.post(
            "/api/v1/register/athlete/",
            format="json",
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(athletes + 1, Athlete.objects.all().count())
        self.assertEqual(users + 1, User.objects.all().count())
        data = response.json()
        self.assertIn("token", data)
        self.assertIsNotNone(data["token"])

    def test_edit_athlete(self):
        athlete = AthleteFactory()
        self.client.force_authenticate(athlete.user)
        data = {
            "first_name": "new_foo",
        }
        response = self.client.patch(
            "/api/v1/athletes/{}/".format(athlete.pk),
            format="json",
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        edited_athlete = Athlete.objects.get(pk=athlete.pk)
        self.assertNotEqual(athlete.first_name, edited_athlete.first_name)
        self.assertEqual(data["first_name"], edited_athlete.first_name)

    def test_not_allow_edit_athlete(self):
        athlete = AthleteFactory()
        self.client.force_authenticate(self.user)
        data = {
            "first_name": "new_foo",
        }
        response = self.client.patch(
            "/api/v1/athletes/{}/".format(athlete.pk),
            format="json",
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_athlete_links(self):
        athlete = AthleteFactory()
        data = {
            "name": "foo",
            "url": "http://example.com",
        }
        self.client.force_authenticate(athlete.user)
        response = self.client.post(
            "/api/v1/links/",
            format="json",
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        athlete = Athlete.objects.get(pk=athlete.pk)
        self.assertEqual(1, athlete.links.count())

    def test_add_athlete_pictures(self):
        athlete = AthleteFactory()
        self.client.force_authenticate(athlete.user)
        picture = Image.new('RGB', (100, 100))
        picture_tmp_file = NamedTemporaryFile(suffix='.jpg')
        picture.save(picture_tmp_file)
        with open(picture_tmp_file.name, 'rb') as picture:
            data = {
                "image": picture,
            }
            response = self.client.post(
                "/api/v1/pictures/",
                format="multipart",
                data=data
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        athlete = Athlete.objects.get(pk=athlete.pk)
        self.assertEqual(1, athlete.pictures.count())

    def test_follow_athlete(self):
        supporter = SupporterFactory()
        athlete = AthleteFactory()
        self.client.force_authenticate(supporter.user)
        response = self.client.post(
            "/api/v1/athletes/{}/follow/".format(athlete.pk),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        supporter = Supporter.objects.get(pk=supporter.pk)
        self.assertEqual(1, supporter.following.all().count())

    def test_followed_by_filter(self):
        AthleteFactory.create_batch(size=10)
        supporter = SupporterFactory()
        athlete = AthleteFactory()
        supporter.follow(athlete)
        self.client.force_authenticate(athlete.user)
        response = self.client.get(
            "/api/v1/athletes/?followed_by={}".format(supporter.user.pk),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(1, data['count'])

    def test_list_reviews(self):
        athlete = AthleteFactory()
        reviews = ReviewFactory.create_batch(athlete=athlete, size=10)
        self.client.force_authenticate(athlete.user)
        response = self.client.get(
            "/api/v1/reviews/",
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(reviews), data['count'])

