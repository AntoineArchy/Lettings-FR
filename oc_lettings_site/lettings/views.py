import logging
import re

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from oc_lettings_site.lettings.models import Letting
from oc_lettings_site.views import log_and_response_error


# Create your views here.
def lettings_index(request: HttpRequest) -> HttpResponse:
    """
    Affiche la liste des locations connues en bdd

    :param request: Objet de requête HTTP Django.
    :return: Les locations connues, affichées dans le template "lettings_index.html".
    """

    try:
        lettings_list = Letting.objects.all()
        if not lettings_list:
            logging.warning("Il semble qu'aucune location ne soit disponible")

        context = {"lettings_list": lettings_list}
        return render(request, "lettings_index.html", context)

    except Exception as e:
        return log_and_response_error(
            request,
            f"Une erreur s'est produite lors de la récupération des locations: {e}",
            "Une erreur s'est produite lors de la récupération des locations.",
            500,
        )


def letting(request: HttpRequest, letting_id: str) -> HttpResponse:
    """
    Récupère les informations sur une location spécifique et les affiche dans la
    vue 'letting.html'.

    :argument:
        request (HttpRequest): L'objet de requête HTTP Django.
        letting_id (int): L'identifiant unique de la location à récupérer.

    :return:
        HttpResponse: La location demandée dans le template 'letting.html'.
    """
    if not re.match("^\\d+$", letting_id):
        return log_and_response_error(
            request,
            f"Une erreur s'est produite lors de la récupération de la location {letting_id} : "
            f"{letting_id} n'est pas interprété comme un id valide",
            "Paramètres de requête invalides.",
            400,
        )

    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "letting.html", context)

    except ObjectDoesNotExist as e:
        return log_and_response_error(
            request,
            f"Une erreur s'est produite lors de la récupération de la locations"
            f" {letting_id} : {e}",
            "La location demandée est introuvable.",
            404,
        )
    except Exception as e:
        return log_and_response_error(
            request,
            f"Une erreur s'est produite lors de la récupération de la locations {letting_id}: {e}",
            f"Une erreur s'est produite lors de la récupération de la locations {letting_id}",
            500,
        )
