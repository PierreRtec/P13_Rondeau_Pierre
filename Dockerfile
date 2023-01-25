FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT=8000

WORKDIR /P13_Rondeau_Pierre

COPY . /P13_Rondeau_Pierre/
COPY . /P13_Rondeau_Pierre/oc_lettings_site/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

CMD ["python", "oc_lettings_site/manage.py", "runserver", "0.0.0.0:8000"]