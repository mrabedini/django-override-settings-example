from django.test import TestCase, override_settings
from django.test.client import RequestFactory

from .views import sample_view

# Create your tests here.
class OverrideSettingsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_without_overriding(self):
        self.__test_sample_view(value_to_be="SETTINGS_VALUE")
    
    @override_settings(SAMPLE_CONFIG="NEW_VALUE")
    def test_with_overriding(self):
        self.__test_sample_view(value_to_be="NEW_VALUE")
    

    def __test_sample_view(self,value_to_be):
        request = self.factory.get("/sample_view/")
        response = sample_view(request)
        self.assertEqual(response.content.decode('utf-8'),value_to_be)
