from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.test import TestCase
from oc_lettings_site.lettings.models import Address, Letting


class LettingModelTest(TestCase):
    def setUp(self):
        Address.objects.create(
            number=42,
            street="Main Street",
            city="Cityville",
            state="CA",
            zip_code=12345,
            country_iso_code="US",
        )

    def test_letting_str(self):
        # Teste la représentation en chaîne du modèle Letting.
        address = Address.objects.get(number=42)
        letting = Letting.objects.create(title="Cozy Apartment", address=address)
        self.assertEqual(str(letting), "Cozy Apartment")

    def test_letting_validation_ok(self):
        # Test de validation avec des valeurs valides
        address = Address.objects.get(number=42)
        letting = Letting(title="TestLocation", address=address)
        self.assertEqual(letting.full_clean(), None)

    def test_letting_validation_ko(self):
        # Test de validation avec des valeurs invalides
        letting = Letting(title="", address=None)
        with self.assertRaises(ValidationError):
            letting.full_clean()

    def test_letting_not_exist(self):
        with self.assertRaises(ObjectDoesNotExist):
            Letting.objects.get(address=42)
