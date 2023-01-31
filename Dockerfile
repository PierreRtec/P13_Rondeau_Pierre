FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /P13_Rondeau_Pierre

COPY . /P13_Rondeau_Pierre/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings
ENV PORT 8000

EXPOSE $PORT

CMD ["gunicorn", "oc-lettings-site.wsgi:application", "--bind", "0.0.0.0:$PORT"]