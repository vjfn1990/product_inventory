clear
clear
clear

docker system prune --force --volumes

# MyProject
docker stop product_inventory-myproject
docker rm product_inventory-myproject
docker rmi product_inventory-myproject

# Django
docker stop product_inventory-django
docker rm product_inventory-django
docker rmi product_inventory-django

docker system prune --force --volumes
