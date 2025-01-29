# word_counter/tests.py
from django.test import TestCase
from django.urls import reverse

class WordCounterTestCase(TestCase):
    def test_word_count(self):
        response = self.client.post(reverse('word_counter'), {'text': 'Hello world!'})
        self.assertContains(response, "Word count: 2")  # Check if word count is correctly displayed
