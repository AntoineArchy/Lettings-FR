from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


# Create your models here.
class Address(models.Model):
    """
    Le modèle Address représente une adresse physique.

    :argument:
        number (int): Le numéro de l'adresse.
        street (str): Le nom de la rue.
        city (str): La ville.
        state (str): L'État.
        zip_code (int): Le code postal.
        country_iso_code (str): Le code ISO du pays.

    :return:
        Une instance d'adresse
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        # db_table = "oc_lettings_site_address"
        verbose_name_plural = "adresses"

    def __str__(self):
        """

        :return: Le numéro et nom de la rue
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    :argument:
        title (str) : Le nom de la location
        adresse (Address) : L'adresse de la location

    :return:
        Une instance de location
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    # class Meta:
    #     db_table = "oc_lettings_site_letting"

    def __str__(self):
        """
        :return:
            Le nom de la location
        """
        return self.title
