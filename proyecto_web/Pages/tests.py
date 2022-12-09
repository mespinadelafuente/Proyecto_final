from django.test import TestCase
import random
import string
from django.contrib.auth.models import User
from .models import Post
 
 
class PostTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="testuser",
            password="12345",
        )
        Post.objects.create(name="Futbol", code=123, owner=self.test_user)
        Post.objects.create(name="Natacion", code=789, owner=self.test_user)
 
        course_test_num = 20
        self.mock_names = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(course_test_num)
        ]
        self.mock_codes = [
            int(
                "".join(
                    [
                        random.choice((string.digits))
                        for _ in range(random.randint(3, 9))
                    ]
                )
            )
            for _ in range(course_test_num)
        ]
 
        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            Post.objects.create(name=mock_name, code=mock_code, owner=self.test_user)
 
    def test_course_model(self):
        """Courses creation are correctly identified"""
        futbol_post = Post.objects.get(name="Futbol")
        natacion_post = Post.objects.get(name="Natacion")
        self.assertEqual(futbol_post.owner.username, "testuser")
        self.assertEqual(natacion_post.owner.username, "testuser")
        self.assertEqual(futbol_post.code, 123)
        self.assertEqual(natacion_post.code, 789)
 
    def test_course_list(self):
        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            course_test = Post.objects.get(name=mock_name)
            self.assertEqual(course_test.owner.username, "testuser")
            self.assertEqual(course_test.code, mock_code)
# Create your tests here.
