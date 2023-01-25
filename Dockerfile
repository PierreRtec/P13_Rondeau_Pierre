FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --ignore-pipfile --python 3.11

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

CMD ["python", "oc_lettings_site/manage.py", "runserver"]