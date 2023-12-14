import logging
import re

from django.core.exceptions import ObjectDoesNotExist
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
    HttpResponseServerError,
)
from django.shortcuts import render

from oc_lettings_site.lettings.models import Letting


def index(request: HttpRequest) -> HttpResponse:
    """
    Affiche la liste des locations connues en bdd

    :param request: Objet de requête HTTP Django.
    :return: Les locations connues, affichées dans le template "lettings/index.html".
    """

    try:
        lettings_list = Letting.objects.all()
        if not lettings_list:
            logging.warning("Il semble qu'aucune location ne soit disponible")

        context = {"lettings_list": lettings_list}
        return render(request, "lettings/index.html", context)

    except Exception as e:
        logging.error(
            f"{request.path} : 500, Une erreur s'est produite lors de la récupération "
            f"des locations: {e}"
        )
        return HttpResponseServerError(
            f"Une erreur s'est produite lors de la récupération des locations."
        )


def letting(request: HttpRequest, letting_id: str) -> HttpResponse:
    """
    Récupère les informations sur une location spécifique et les affiche dans la
    vue 'letting.html'.

    :argument:
        request (HttpRequest): L'objet de requête HTTP Django.
        letting_id (int): L'identifiant unique de la location à récupérer.

    :return:
        HttpResponse: La location demandée dans le template 'lettings/letting.html'.
    """
    if not re.match("^\\d+$", letting_id):
        logging.error(
            f"{request.path} : 400, Une erreur s'est produite lors de la récupération de "
            f"la location {letting_id} : "
            f"{letting_id} n'est pas interprété comme un id valide"
        )
        return HttpResponseBadRequest("Paramètres de requête invalides.")

    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "lettings/letting.html", context)

    except ObjectDoesNotExist as e:
        logging.error(
            f"{request.path} : 404, Une erreur s'est produite lors de la récupération "
            f"de la locations {letting_id} : {e} "
            f"{letting_id} n'est pas interprété comme un id valide"
        )
        return HttpResponseNotFound("La location demandée est introuvable.")
    except Exception as e:
        logging.error(
            f"{request.path} : 500, Une erreur s'est produite lors de la récupération de la "
            f"locations {letting_id}: {e}"
        )
        return HttpResponseServerError(
            f"Une erreur s'est produite lors de la récupération de la locations {letting_id}"
        )
