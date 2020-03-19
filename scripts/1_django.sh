clear
clear
clear

docker stop product_inventory-django
docker rm product_inventory-django
docker rmi product_inventory-django

cd $(pwd)/../composers/django
docker-compose up
