FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /P13_Rondeau_Pierre

COPY . /P13_Rondeau_Pierre/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN cd .\oc_lettings_site\

ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

CMD ["python", "manage.py", "runserver"]