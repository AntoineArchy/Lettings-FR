import logging

from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.shortcuts import render


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
