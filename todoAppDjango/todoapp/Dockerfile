FROM python:3.9-alpine

RUN apk update \
  && apk add \
    build-base \
    libpq \
    py3-pip

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
# ENV PIP_ROOT_USER_ACTION=ignore
# ENV PIP_DISABLE_ROOT_WARNING on

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
