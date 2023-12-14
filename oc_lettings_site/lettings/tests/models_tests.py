from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.test import TestCase
from oc_lettings_site.lettings.models import Address, Letting


class LettingModelTest(TestCase):
    def setUp(self):
        # Il nous faut une Adresse valide pour tester le comportement du model
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
        # Test que l'Exception attendue est levée en cas d'objet inexistant
        with self.assertRaises(ObjectDoesNotExist):
            Letting.objects.get(address=42)


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
