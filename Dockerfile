FROM django

COPY . .

CMD python manage.py runserver