FROM python:3.10

WORKDIR /P13_Rondeau_Pierre

COPY . /P13_Rondeau_Pierre/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.oc_lettings_site.settings
CMD ["python", "oc_lettings_site/manage.py", "collectstatic", "--noinput"]
CMD ["gunicorn", "oc_lettings_site.oc_lettings_site.wsgi"]
