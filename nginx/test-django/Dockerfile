FROM python:3

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /app/

CMD ["python", "managy.py", "collectstatic"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "conf.wsgi:application"]

EXPOSE 8000
