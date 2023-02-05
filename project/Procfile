release: python manage.py migrate
web: gunicorn -w 4 gimme.wsgi:application