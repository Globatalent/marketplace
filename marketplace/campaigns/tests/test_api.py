import datetime

from PIL import Image
from django.core.files.temp import NamedTemporaryFile
from rest_framework import status
from rest_framework.test import APITestCase

from marketplace.campaigns.constants import ATHLETE, APPROVED
from marketplace.campaigns.models import Campaign
from marketplace.campaigns.tests.factories import CampaignFactory
from marketplace.users.models import User
from marketplace.users.tests.factories import UserFactory


class CampaignAPITests(APITestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_create_campaign(self):
        campaigns = Campaign.objects.all().count()
        picture = Image.new('RGB', (100, 100))
        picture_tmp_file = NamedTemporaryFile(suffix='.jpg')
        picture.save(picture_tmp_file)
        with open(picture_tmp_file.name, 'rb') as picture:
            data = {
                "title": "foo",
                "kind": ATHLETE,
                "description": "foo",
                "image": picture,
                "tags": ["tag"]
            }
            self.client.force_authenticate(self.user)
            response = self.client.post(
                "/api/v1/campaigns/",
                format="multipart",
                data=data,
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(campaigns + 1, Campaign.objects.all().count())
        campaign = response.json()
        self.assertIn("token", campaign)
        self.assertEqual(len(data["tags"]), len(campaign["tags"]))

    def test_edit_campaign(self):
        campaign = CampaignFactory(user=self.user)
        self.client.force_authenticate(self.user)
        data = {
            "title": "new title",
        }
        response = self.client.patch(
            "/api/v1/campaigns/{}/".format(campaign.pk),
            format="json",
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        edited_campaign = Campaign.objects.get(pk=campaign.pk)
        self.assertNotEqual(campaign.title, edited_campaign.title)
        self.assertEqual(data["title"], edited_campaign.title)

    def test_edit_campaign_tags(self):
        campaign = CampaignFactory(user=self.user)
        self.client.force_authenticate(self.user)
        data = {
            "tags": [
                "tag 1",
                "tag 2",
                "tag 3",
            ],
        }
        response = self.client.patch(
            "/api/v1/campaigns/{}/".format(campaign.pk),
            format="json",
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        edited_campaign = Campaign.objects.get(pk=campaign.pk)
        self.assertEqual(len(data["tags"]), edited_campaign.tags.count())

    def test_not_allow_edit_campaign(self):
        campaign = CampaignFactory(user=self.user)
        self.client.force_authenticate(UserFactory())
        data = {
            "title": "new title",
        }
        response = self.client.patch(
            "/api/v1/campaigns/{}/".format(campaign.pk),
            format="json",
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_campaign_links(self):
        campaign = CampaignFactory(user=self.user)
        data = {
            "campaign": campaign.pk,
            "name": "foo",
            "url": "http://example.com",
        }
        self.client.force_authenticate(self.user)
        response = self.client.post(
            "/api/v1/links/",
            format="json",
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        campaign = Campaign.objects.get(pk=campaign.pk)
        self.assertEqual(1, campaign.links.count())

    def test_add_campaign_revenues(self):
        campaign = CampaignFactory(user=self.user)
        data = {
            "campaign": campaign.pk,
            "year": 2014,
            "amount": 100.0,
        }
        self.client.force_authenticate(self.user)
        response = self.client.post(
            "/api/v1/revenues/",
            format="json",
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        campaign = Campaign.objects.get(pk=campaign.pk)
        self.assertEqual(1, campaign.revenues.count())

    def test_add_campaign_incomes(self):
        campaign = CampaignFactory(user=self.user)
        data = {
            "campaign": campaign.pk,
            "year": 2020,
            "amount": 100.0,
        }
        self.client.force_authenticate(self.user)
        response = self.client.post(
            "/api/v1/incomes/",
            format="json",
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        campaign = Campaign.objects.get(pk=campaign.pk)
        self.assertEqual(1, campaign.incomes.count())

    def test_add_campaign_recommendations(self):
        campaign = CampaignFactory(user=self.user)
        picture = Image.new('RGB', (100, 100))
        picture_tmp_file = NamedTemporaryFile(suffix='.jpg')
        picture.save(picture_tmp_file)
        with open(picture_tmp_file.name, 'rb') as picture:
            data = {
                "campaign": campaign.pk,
                "file": picture,
            }
            self.client.force_authenticate(self.user)
            response = self.client.post(
                "/api/v1/recommendations/",
                format="multipart",
                data=data
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        campaign = Campaign.objects.get(pk=campaign.pk)
        self.assertEqual(1, campaign.recommendations.count())

    def test_add_campaign_pictures(self):
        campaign = CampaignFactory(user=self.user)
        self.client.force_authenticate(self.user)
        picture = Image.new('RGB', (100, 100))
        picture_tmp_file = NamedTemporaryFile(suffix='.jpg')
        picture.save(picture_tmp_file)
        with open(picture_tmp_file.name, 'rb') as picture:
            data = {
                "campaign": campaign.pk,
                "image": picture,
            }
            response = self.client.post(
                "/api/v1/pictures/",
                format="multipart",
                data=data
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        campaign = Campaign.objects.get(pk=campaign.pk)
        self.assertEqual(1, campaign.pictures.count())

    def test_follow_campaign(self):
        campaign = CampaignFactory()
        user = UserFactory()
        self.client.force_authenticate(user)
        response = self.client.post(
            "/api/v1/campaigns/{}/follow/".format(campaign.pk),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(pk=user.pk)
        self.assertEqual(1, user.following.all().count())

    def test_followed_by_filter(self):
        user = UserFactory()
        CampaignFactory.create_batch(size=10)
        campaign = CampaignFactory()
        user.follow(campaign)
        self.client.force_authenticate(user)
        response = self.client.get(
            "/api/v1/campaigns/?followed_by={}".format(user.pk),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(1, data['count'])

    def test_followed_is_draft(self):
        user = UserFactory()
        CampaignFactory.create_batch(is_draft=True, size=10)
        campaign = CampaignFactory(is_draft=False)
        user.follow(campaign)
        self.client.force_authenticate(user)
        response = self.client.get(
            "/api/v1/campaigns/?is_draft=False",
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(1, data['count'])

    def test_list_search_campaigns(self):
        other_campaigns = CampaignFactory.create_batch(title="other title", description="other description", size=10)
        foo_campaigns = CampaignFactory.create_batch(title="foo title", description="foo description", size=5)
        CampaignFactory(title="one title", description="one description")
        response = self.client.get(
            "/api/v1/campaigns/?search=other",
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(other_campaigns), data['count'])
        response = self.client.get(
            "/api/v1/campaigns/?search=foo",
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(foo_campaigns), data['count'])
        response = self.client.get(
            "/api/v1/campaigns/?search=one",
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(1, data['count'])

    def test_list_active_campaigns(self):
        active_campaigns = CampaignFactory.create_batch(is_draft=False, size=10)
        for campaign in active_campaigns:
            campaign.state = APPROVED
            campaign.save()
        inactive_campaigns = CampaignFactory.create_batch(is_draft=False, size=5)
        for campaign in inactive_campaigns:
            campaign.state = APPROVED
            campaign.save()
            campaign.started = datetime.date.today() - datetime.timedelta(days=10)
            campaign.finished = datetime.date.today() - datetime.timedelta(days=1)
            campaign.save()
        response = self.client.get(
            "/api/v1/campaigns/?active=True",
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(active_campaigns), data['count'])
        response = self.client.get(
            "/api/v1/campaigns/?active=False",
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(inactive_campaigns), data['count'])
