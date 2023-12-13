import logging

from django.test import TestCase
from django.urls import reverse

from oc_lettings_site.lettings.models import Address, Letting


class LettingsIndexViewTest(TestCase):
    def setUp(self):
        address = Address.objects.create(
            number=42,
            street="Main Street",
            city="Cityville",
            state="CA",
            zip_code=12345,
            country_iso_code="US",
        )
        Letting.objects.create(title="Location 1", address=address)

    def test_lettings_index_view(self):
        url = reverse("lettings_index")
        response = self.client.get(url)

        # Vérifie que la réponse a un code HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Vérifie que la réponse utilise le bon template
        self.assertTemplateUsed(response, "lettings_index.html")

        # Vérifie que les locations sont présentes dans le contexte
        self.assertIn("lettings_list", response.context)

        # Vérifie que le contexte contient la liste des locations
        lettings_list = response.context["lettings_list"]

        self.assertEqual(len(lettings_list), 1)

    def test_no_letting_warning(self):
        # Supprimez les profils existants pour simuler l'absence de profils

        Address.objects.all().delete()

        url = reverse("lettings_index")
        with self.assertLogs(logger=logging.getLogger(), level="WARNING") as cm:
            self.client.get(url)
        self.assertIn("Il semble qu'aucune location ne soit disponible", cm.output[0])


class LettingViewTest(TestCase):
    def setUp(self):
        address = Address.objects.create(
            number=42,
            street="Main Street",
            city="Cityville",
            state="CA",
            zip_code=12345,
            country_iso_code="US",
        )
        Letting.objects.create(title="Location 1", address=address)

    def test_valid_letting_id(self):
        # Utilise reverse pour obtenir l'URL avec un ID de location valide
        url = reverse("letting", args=["1"])
        response = self.client.get(url)

        # Vérifie que la réponse a un code HTTP 200 (OK) et utilise le bon template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "letting.html")

    def test_invalid_letting_id(self):
        # Utilise reverse pour obtenir l'URL avec un ID de location invalide
        url = reverse("letting", args=["invalid_id"])
        response = self.client.get(url)

        # Vérifie que la réponse a un code HTTP 400 (Bad Request) et contient le bon message
        # d'erreur
        self.assertEqual(response.status_code, 400)
        self.assertIn("Paramètres de requête invalides.", response.content.decode())

    def test_nonexistent_letting_id(self):
        # Utilise reverse pour obtenir l'URL avec un ID de location inexistant
        url = reverse("letting", args=["999"])
        response = self.client.get(url)

        # Vérifie que la réponse a un code HTTP 404 (Not Found) et contient le bon message d'erreur
        self.assertEqual(response.status_code, 404)
        self.assertIn("La location demandée est introuvable.", response.content.decode())
