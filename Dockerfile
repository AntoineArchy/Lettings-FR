FROM python:3.10
LABEL authors="AntoineTsz"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 3000

# Commande par défaut à exécuter lors du démarrage du conteneur
CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]
