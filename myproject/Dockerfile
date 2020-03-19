FROM product_inventory-django:latest
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY myproject/entrypoint.sh /app
RUN django-admin startproject myproject
WORKDIR /app/myproject
RUN python manage.py startapp myapp
COPY src/myproject/myapp myapp
COPY src/myproject/myproject myproject
RUN python manage.py makemigrations myapp
RUN python manage.py migrate
