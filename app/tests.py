from django.test import TestCase
from django.urls import reverse
from RecQuiz.models import Course


# Create your tests here.
class CourseViewTests(TestCase):
    def test_no_course_views(self):
        """
        If no courses exist, the appropriate message should be displayed.
        """
        response = self.client.get(reverse('RecQuiz:courses'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are not new courses.')
        self.assertQuerysetEqual(response.context['courses'], [])

    def add_courses(self, c_id, coordinator, course_name, slug):
        course = Course.objects.get_or_create(course_id = c_id)[0]
        course.coordinator = coordinator
        course.course_name = course_name
        course.slug = slug
        course.save()
        return course

    def test_courses_view(self):
        """
        Checks whether courses are displayed correctly when present.
        """
        self.add_courses(1, 'professer1', 'course1', 'course-1')
        self.add_courses(2, 'professer2', 'course2', 'course-2')
        self.add_courses(3, 'professer3', 'course3', 'course-3')
        response = self.client.get(reverse('RecQuiz:courses'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "professer1")
        self.assertContains(response, "professer2")
        self.assertContains(response, "professer3")
        self.assertContains(response, "course1")
        self.assertContains(response, "course2")
        self.assertContains(response, "course3")
        self.assertContains(response, 'START LEARNING')
        self.assertContains(response, 'DELETE COURSE')
        num_courses = len(response.context['courses'])
        self.assertEquals(num_courses, 3)
class MyCourseViewTests(TestCase):
    def test_no_course_views(self):
        """
        If no courses exist, the appropriate message should be displayed.
        """
        response = self.client.get(reverse('RecQuiz:my_course'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'You have not registered any course.')
        self.assertQuerysetEqual(response.context['courses'], [])

    def add_courses(self, c_id, coordinator, course_name, slug):
        course = Course.objects.get_or_create(course_id = c_id)[0]
        course.coordinator = coordinator
        course.course_name = course_name
        course.slug = slug
        course.save()
        return course

    def test_courses_view(self):
        """
        Checks whether courses are displayed correctly when present.
        """
        self.add_courses(1, 'professer1', 'course1', 'course-1')
        self.add_courses(2, 'professer2', 'course2', 'course-2')
        self.add_courses(3, 'professer3', 'course3', 'course-3')
        response = self.client.get(reverse('RecQuiz:my_course'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "professer1")
        self.assertContains(response, "professer2")
        self.assertContains(response, "professer3")
        self.assertContains(response, "course1")
        self.assertContains(response, "course2")
        self.assertContains(response, "course3")
        self.assertContains(response, 'Start')
        self.assertContains(response, 'Delete')
        num_courses = len(response.context['courses'])
        self.assertEquals(num_courses, 3)