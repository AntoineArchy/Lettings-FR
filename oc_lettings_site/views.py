import logging
import re

from django.core.exceptions import ObjectDoesNotExist
from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.shortcuts import render

from .models import Letting, Profile


def log_and_response_error(
    request: HttpRequest, log_message: str, response_message: str, status_code: int
):
    logging.error(f"{request.path} : {status_code}, {log_message}")
    return HttpResponse(status=status_code, content=response_message)


def index(request: HttpRequest) -> HttpResponse:
    """
    Affiche la page d'accueil de l'application

    :param request: Objet de requête HTTP Django.
    :return: La page d'accueil en utilisant le template 'index.html'
    """
    return render(request, "index.html")


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
    Récupère les informations sur une location spécifique et les affiche dans la vue 'letting.html'.

    :argument:
        request (HttpRequest): L'objet de requête HTTP Django.
        letting_id (int): L'identifiant unique de la location à récupérer.

    :return:
        HttpResponse: La location demandée dans le template 'letting.html'.
    """
    if not re.match("^\d+$", letting_id):
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
            f"Une erreur s'est produite lors de la récupération de la locations {letting_id} : {e}",
            "La location demandée est introuvable.",
            404,
        )


def profiles_index(request: HttpRequest) -> HttpResponse:
    """
    Affiche la liste des profils utilisateur connus dans la base de données.

    :param request: Objet de requête HTTP Django.
    :return: Réponse HTTP avec la liste des profils rendue dans le template "profiles_index.html".
    """
    try:
        profiles_list = Profile.objects.all()
        if not profiles_list:
            logging.warning("Il semble qu'aucun profil n'est disponible")
        context = {"profiles_list": profiles_list}
        return render(request, "profiles_index.html", context)

    except Exception as e:
        return log_and_response_error(
            request,
            f"Une erreur s'est produite lors de la récupération des profiles: {e}",
            "Une erreur s'est produite lors de la récupération des profiles.",
            500,
        )


def profile(request: HttpRequest, username: str) -> HttpResponse:
    """
    Affiche le profil utilisateur correspondant au nom d'utilisateur demandé.

    :param request: Objet de requête HTTP Django.
    :param username: Nom d'utilisateur du profil à afficher.
    :return: Réponse HTTP avec le profil rendu dans le template "profile.html".
    """

    try:
        profile = Profile.objects.get(user__username=username)
        context = {"profile": profile}
        return render(request, "profile.html", context)

    except ObjectDoesNotExist as e:
        return log_and_response_error(
            request,
            f"Une erreur s'est produite lors de la récupération du profil de {username} : {e}",
            "Le profil demandé est introuvable.",
            404,
        )
    except Exception as e:
        return log_and_response_error(
            request,
            f"Une erreur s'est produite lors de la récupération du profil de {username} : {e}",
            "Paramètres de requête invalides.",
            500,
        )
