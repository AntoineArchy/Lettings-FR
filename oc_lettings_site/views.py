import logging

from django.core.exceptions import ObjectDoesNotExist
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseServerError,
    HttpResponseNotFound,
    HttpResponseBadRequest,
)
from django.shortcuts import render

from .models import Letting, Profile


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
        logging.error(f"Une erreur s'est produite lors de la récupération des locations: {e}")
        return HttpResponseServerError(
            "Une erreur s'est produite lors de la récupération des locations."
        )


def letting(request: HttpRequest, letting_id: int) -> HttpResponse:
    """
    Récupère les informations sur une location spécifique et les affiche dans la vue 'letting.html'.

    :argument:
        request (HttpRequest): L'objet de requête HTTP Django.
        letting_id (int): L'identifiant unique de la location à récupérer.

    :return:
        HttpResponse: La location demandée dans le template 'letting.html'.
    """

    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "letting.html", context)

    except ObjectDoesNotExist as e:
        logging.error(
            f"Une erreur s'est produite lors de la récupération de la locations {letting_id} : {e}"
        )
        return HttpResponseNotFound("La location demandée est introuvable.")

    except ValueError as e:
        logging.error(
            f"Une erreur s'est produite lors de la récupération de la location {letting_id} : {e}"
        )
        return HttpResponseBadRequest("Paramètres de requête invalides.")


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
        logging.error(f"Une erreur s'est produite lors de la récupération des profiles: {e}")
        return HttpResponseServerError(
            "Une erreur s'est produite lors de la récupération des profiles."
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
        logging.error(
            f"Une erreur s'est produite lors de la récupération du profil de {username} : {e}"
        )
        return HttpResponseNotFound("Le profil demandé est introuvable.")

    except ValueError as e:
        logging.error(
            f"Une erreur s'est produite lors de la récupération du profil de {username} : {e}"
        )
        return HttpResponseBadRequest("Paramètres de requête invalides.")
