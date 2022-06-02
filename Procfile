
release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: daphne delivameals.asgi:application 