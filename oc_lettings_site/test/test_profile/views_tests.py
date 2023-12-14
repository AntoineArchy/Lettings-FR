import logging
from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from oc_lettings_site.models import Profile


class ProfilesIndexViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="john_doe", password="password123")
        self.profile1 = Profile.objects.create(user=user, favorite_city="Lille")

    def test_profiles_index_view(self):
        url = reverse("profiles_index")
        response = self.client.get(url)

        # Vérifie que la réponse a un code HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Vérifie que la réponse utilise le bon template
        self.assertTemplateUsed(response, "profiles_index.html")

        # Vérifie que les profiles sont présents dans le contexte
        self.assertIn("profiles_list", response.context)

        # Vérifie que le contexte contient la liste des profils
        profiles_list = response.context["profiles_list"]

        # Vérifie que la liste est correcte
        self.assertEqual(list(profiles_list), [self.profile1])

    def test_no_profile_warning(self):
        # Supprimez les profils existants pour simuler l'absence de profils
        Profile.objects.all().delete()

        url = reverse("profiles_index")
        with self.assertLogs(logger=logging.getLogger(), level="WARNING") as cm:
            self.client.get(url)
        self.assertIn("Il semble qu'aucun profil n'est disponible", cm.output[0])

    @patch("oc_lettings_site.views.Profile.objects.all")
    def test_unhandled_exception_in_view(self, mock_get):
        # Configurez le comportement du mock pour lever une exception
        mock_get.side_effect = Exception("Une erreur simulée")

        # Utilisez reverse pour obtenir l'URL avec un ID de location
        url = reverse("profiles_index")

        # Utilisez with self.assertRaises() pour capturer l'exception attendue
        response = self.client.get(url)

        # Vous pouvez également vérifier le code de statut dans la réponse si nécessaire
        self.assertEqual(response.status_code, 500)  # Ou le code de statut attendu


class ProfileViewTest(TestCase):
    def setUp(self):
        # Créez un objet de modèle pour tester
        self.user = User.objects.create(username="testuser")
        self.profile = Profile.objects.create(user=self.user)

    def test_profile_view_with_valid_profile(self):
        url = reverse("profile", args=["testuser"])
        response = self.client.get(url)

        # Vérifie que le code de statut de la réponse est correct et utilise le bon template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profile.html")

        # Vérifie que le modèle de profil est présent dans le contexte
        self.assertIn("profile", response.context)
        profile_context = response.context["profile"]

        self.assertEqual(profile_context, self.profile)

    def test_profile_view_with_nonexistent_profile(self):
        url = reverse("profile", args=["nonexistentuser"])
        response = self.client.get(url)

        # Assurez-vous que le code de statut de la réponse est correct
        self.assertEqual(response.status_code, 404)
        self.assertIn("Le profil demandé est introuvable.", response.content.decode())

    @patch("oc_lettings_site.views.Profile.objects.get")
    def test_unhandled_exception_in_view(self, mock_get):
        # Configurez le comportement du mock pour lever une exception
        mock_get.side_effect = Exception("Une erreur simulée")

        # Utilisez reverse pour obtenir l'URL avec un ID de location
        url = reverse("profile", args=["AnyArgs"])

        # Utilisez with self.assertRaises() pour capturer l'exception attendue
        response = self.client.get(url)

        # Vous pouvez également vérifier le code de statut dans la réponse si nécessaire
        self.assertEqual(response.status_code, 500)  # Ou le code de statut attendu
