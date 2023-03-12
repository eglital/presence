FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

# COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# COPY ./api /app/api

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
