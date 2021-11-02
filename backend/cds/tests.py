from django.test import TestCase  # noqa: F401

from .models import Lecture

# Create your tests here.


class LectureTestCase(TestCase):
    def setUp(self):
        Lecture.objects.create(
            title="Factory Physics: Methods for Efficient Project Management in a Scientific Environment",
            date="2021-10-27",
            corporate_author="CERN. Geneva",
            abstract="As the architect of Chevron’s major capital project system which was used to guide development and execution of about $500 Billion US dollars of projects, Gary became frustrated with the poor cost and schedule performance of those investments and launched a search for something better. &nbsp;In his search he discovered Project Production Management based on Factory Physics and Operations Science.&nbsp; After using PPM to rescue several projects that were years behind schedule and 100’s of millions over budget, he began to implement PPM throughout Chevron.&nbsp; </span></span></span></p> <p><span><span><span>In this lecture Gary will describe his personal journey that took him beyond those industries that use conventional “best practice” project management methods to focus on how manufacturing industries have realized multi fold increases in productivity over the years and to adapt their underlying principles to complex construction projects in the energy sector.",
            series="(Academic Training Lecture Regular Programme ; 2021-2022)",
            speaker="Fischer, PE, Gary",
            speaker_details="Factory Physics",
            event_details="https://indico.cern.ch/event/1065792/",
            thumbnail_picture="http://mediaarchive.cern.ch/MediaArchive/Video/Public/Conferences/2021/1065792/legacy.jpg",
            language="eng",
            subject_category="Academic Training Lecture Regular Programme",
            lecture_note="on 2021-10-27T16:00:00",
            imprint="2021-10-27. - 1:06:01.",
            license="© 2021 CERN",
        )

        Lecture.objects.create(
            title="Dark Matter searches",
            date="2021-07-01",
            corporate_author="CERN. Geneva",
            abstract="Dark Matter is one of the most compelling motivations for physics beyond the Standard Model. This lecture series will review the status and prospects for Dark Matter searches, covering both direct and indirect searches. The lectures will review searches over the full mass range of possible Dark Matter candidates, covering the different techniques used in these searches. In addition future prospects for these searches will be presented.",
            series="(Academic Training Lecture Regular Programme ; 2020-2021)",
            speaker="Tovey, Daniel",
            speaker_details="University of Sheffield",
            event_details="https://indico.cern.ch/event/870610",
            thumbnail_picture="http://mediaarchive.cern.ch/MediaArchive/Video/Public/Conferences/2021/870610/870610-thumbnail-179x101-at-100-percent.jpg",
            language="eng",
            subject_category="Academic Training Lecture Regular Programme",
            lecture_note="on 2021-07-01T11:00:00",
            imprint="2021-07-01. - 0:56:59",
            license="© 2021 CERN",
        )

    def test_lectures_display(self):
        lecture1 = Lecture.objects.get(name="lecture1")
        lecture2 = Lecture.objects.get(name="lecture2")
        self.assertEqual(lecture1.display(), "")
        self.assertEqual(lecture2.display(), "")
