from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.test import TestCase

from oc_lettings_site.models import Address


class AddressModelTest(TestCase):
    def setUp(self):
        Address.objects.create(
            number=123,
            street="Main St",
            city="Cityville",
            state="CA",
            zip_code=12345,
            country_iso_code="USA",
        )

    def test_address_str_method(self):
        address = Address.objects.get(number=123)
        self.assertEqual(str(address), "123 Main St")

    def test_address_validation_ok(self):
        # Test de validation avec des valeurs valides
        address = Address(
            number=456,
            street="Second St",
            city="Townsville",
            state="NY",
            zip_code=54321,
            country_iso_code="USA",
        )
        self.assertEqual(address.full_clean(), None)

    def test_address_validation_ko(self):
        # Test de validation avec des valeurs invalides
        address = Address(
            number=10000,  # Valeur supérieure à la limite définie
            street="",  # Champ requis vide
            city="",  # Champ requis vide
            state="California",  # Valeur trop longue pour le champ state
            zip_code=-1,  # Valeur négative non autorisée
            country_iso_code="US",  # Valeur trop courte pour le champ country_iso_code
        )
        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_address_not_exist(self):
        with self.assertRaises(ObjectDoesNotExist):
            Address.objects.get(zip_code=42)
