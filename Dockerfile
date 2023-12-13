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

# Commande par défaut à exécuter lors du démarrage du conteneur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
