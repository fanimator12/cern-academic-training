from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Lecture

# Create your tests here.


class LectureTest(APITestCase):
    def setUp(self):
        self.url = "/api/lectures/"
        # self.username = 'admin'
        # self.password = '123456'
        # self.user = User.objects.create_user(self.username, self.password)
        # self.token = Token.objects.create(user=self.user)
        # self.api_authentication()

        self.load = {
            "lecture_id": "2788942",
            "title": "REMOTE: Federated Data Architectures",
            "date": "2021-10-22",
            "corporate_author": "This is an author",
            "abstract": "TEST",
            "series": "(Academic Training Lecture Regular Programme ; 202",
            "speaker": "de Jong, Michiel",
            "speaker_details": "Speakers details",
            "event_details": "Event Details",
            "thumbnail_picture": "http://mediaarchive.cern.ch/MediaArchive/Video/Public/Conferences/2021/1049666/1049666-presenter-cover.png",
            "language": "eng",
            "subject_category": "Academic Training Lecture Regular Programme",
            "lecture_note": "2021-10-22T11:59:35Z",
            "imprint": "01:03:18",
            "license": "© 2021 CERN",
        }

        # self.object = Lecture.objects.create(**self.load)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_get_lectures(self):

        # get API response
        response = self.client.get(self.url, format="json")

        # get data from db
        # lectures = Lecture.objects.all()
        # serializer = LectureSerializer(lectures, many=True)

        self.assertEqual(response.data, self.object)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_lecture(self):

        data = self.load

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_lecture(self):
        # /api/lectures/<int:pk>
        url = reverse("lecture_details", kwargs={"pk": "2782916"})

        response = self.client.get(url, pk="2782916", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lecture.objects.count(), 1)
        self.assertEqual(Lecture.objects.get().lecture_id, "2782916")


# make tests with these: POST /lecture, /lectures/<int:pk> , /lectures
