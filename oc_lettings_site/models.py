from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    :argument:
        user (User) : L'instance d'un utilisateur défault de Django
        favorite_city (str) : Le nom de la ville favorite de l'utilisateur

    :return:
        Une instance de Profile

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """

        :return: Le nom d'utilisateur
        """
        return self.user.username
