FROM python:3.11-slim-buster

WORKDIR /P13_Rondeau_Pierre

COPY . /P13_Rondeau_Pierre/
COPY . /P13_Rondeau_Pierre/oc_lettings_site/

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --ignore-pipfile --python 3.11

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE oc_lettings_site.settings

CMD ["python", "oc_lettings_site/manage.py", "runserver"]