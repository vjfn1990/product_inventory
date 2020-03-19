clear
clear
clear

docker stop product_inventory-myproject
docker rm product_inventory-myproject
docker rmi product_inventory-myproject

cd $(pwd)/../composers/myproject
docker-compose up
