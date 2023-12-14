import logging
from unittest.mock import patch

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
        # Test que la vue est accessible et retourne l'ensemble des données
        url = reverse("lettings_index")
        response = self.client.get(url)

        # Vérifie que la réponse a un code HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Vérifie que la réponse utilise le bon template
        self.assertTemplateUsed(response, "lettings/index.html")

        # Vérifie que les locations sont présentes dans le contexte
        self.assertIn("lettings_list", response.context)

        # Vérifie que le contexte contient la liste des locations
        lettings_list = response.context["lettings_list"]

        # Vérifie que l'ensemble du listing est présent
        self.assertEqual(len(lettings_list), 1)

    def test_no_letting_warning(self):
        # Test l'avertissement si aucune location n'est présente en base

        # Supprimez les profils existants pour simuler l'absence de profils
        Address.objects.all().delete()

        url = reverse("lettings_index")
        with self.assertLogs(logger=logging.getLogger(), level="WARNING") as cm:
            self.client.get(url)
        self.assertIn("Il semble qu'aucune location ne soit disponible", cm.output[0])

    @patch("oc_lettings_site.lettings.views.Letting.objects.all")
    def test_unhandled_exception_in_view(self, mock_get):
        # Test que la vue répond bien en cas d'exception non gérée

        # Configurez le comportement du mock pour lever une exception
        mock_get.side_effect = Exception("Une erreur simulée")

        url = reverse("lettings_index")
        response = self.client.get(url)

        # Vérifie que la réponse a un code HTTP 500 (Internal Server Error)
        self.assertEqual(response.status_code, 500)

        # Vérifie que l'avertissement est présent
        self.assertContains(
            response, "Une erreur s'est produite lors de la récupération des locations."
        )


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
        # Test que la vue est accessible et retourne l'ensemble des données

        url = reverse("letting", args=["1"])
        response = self.client.get(url)

        # Vérifie que la réponse a un code HTTP 200 (OK) et utilise le bon template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")

    def test_invalid_letting_id(self):
        # Test le comportement de la vue en cas d'ID transmis non valide
        url = reverse("letting", args=["invalid_id"])
        response = self.client.get(url)

        # Vérifie que la réponse a un code HTTP 400 (Bad Request) et contient le bon message
        # d'erreur
        self.assertEqual(response.status_code, 400)
        self.assertIn("Paramètres de requête invalides.", response.content.decode())

    def test_nonexistent_letting_id(self):
        # Test le comportement de la vue en cas d'ID transmis valide, mais non existant

        url = reverse("letting", args=["999"])
        response = self.client.get(url)

        # Vérifie que la réponse a un code HTTP 404 (Not Found) et contient le bon message d'erreur
        self.assertEqual(response.status_code, 404)
        self.assertIn("La location demandée est introuvable.", response.content.decode())

    @patch("oc_lettings_site.lettings.views.Letting.objects.get")
    def test_unhandled_exception_in_view(self, mock_get):
        # Test que la vue répond bien en cas d'exception non gérée

        # Configurez le comportement du mock pour lever une exception
        mock_get.side_effect = Exception("Une erreur simulée")

        # Utilisez reverse pour obtenir l'URL avec un ID de location
        url = reverse("letting", args=["1"])

        # Utilisez with self.assertRaises() pour capturer l'exception attendue
        response = self.client.get(url)

        # Vous pouvez également vérifier le code de statut dans la réponse si nécessaire
        self.assertEqual(response.status_code, 500)  # Ou le code de statut attendu
