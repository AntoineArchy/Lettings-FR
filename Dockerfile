FROM python:3.10
LABEL authors="AntoineTsz"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python manage.py makemigrations
RUN python manage.py migrate

#RUN python manage.py collectstatic --noinput


EXPOSE 8000
# Récupération des fichiers statiques
RUN python3 manage.py collectstatic --noinput
# Commande par défaut à exécuter lors du démarrage du conteneur
CMD ["sh", "-c", "python3 manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]