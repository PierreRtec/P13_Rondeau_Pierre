FROM python:3.10

WORKDIR /P13_Rondeau_Pierre

COPY . /P13_Rondeau_Pierre/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.oc_lettings_site.settings
ENV PORT=8000

CMD ["gunicorn", "oc_lettings_site.oc_lettings_site.wsgi", "--bind", "0.0.0.0:8000"]