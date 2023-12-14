from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """
    Affiche la page d'accueil de l'application

    :param request: Objet de requête HTTP Django.
    :return: La page d'accueil en utilisant le template 'index.html'
    """
    return render(request, "index.html")


def oc_lettings_site_404(request, exception):
    return render(request, "404.html", status=404)


def oc_lettings_site_400(request, exception):
    return render(request, "400.html", status=404)


def oc_lettings_site_500(request):
    return render(request, "500.html", status=500)
