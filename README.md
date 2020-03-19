# Product Inventory

Dockerized Python/Django webapp, that shows how to make some CRUD operations using Django Models

## Installation and execution

'docker' and 'docker-compose' need to be installed, to be able to deploy the webapp

```bash
git clone https://github.com/vjfn1990/product_inventory.git
cd product_inventory/scripts
./0_cleaner.sh
./1_django.sh
./2_myproject.sh
```

These scripts need to be executed by the order given on their names. They clean and deploy the corresponding Docker containers over the network "product_inventory-network"

Once the last container is listening, on a browser the URL [http://localhost:6868/myapp](http://localhost:6868/myapp) can be displayed

## Project tree

```bash
.
├── composers
│   ├── django
│   │   └── docker-compose.yml
│   └── myproject
│       └── docker-compose.yml
├── django
│   └── Dockerfile
├── myproject
│   ├── Dockerfile
│   └── entrypoint.sh
├── README.md
├── scripts
│   ├── 0_cleaner.sh
│   ├── 1_django.sh
│   └── 2_myproject.sh
└── src
    └── myproject
        ├── myapp
        │   ├── models.py
        │   ├── static
        │   │   └── myapp
        │   ├── templates
        │   │   └── myapp
        │   │       └── central.html
        │   ├── urls.py
        │   └── views.py
        └── myproject
            ├── settings.py
            └── urls.py
```

## Example URLs to test the API endpoints

Sample Filling:

http://localhost:6868/myapp/sample_filling

Register:

http://localhost:6868/myapp/register?sku=W0X1Y2Z2&name=chicken&qty=8&price=6.75

Retrieve from sku:

http://localhost:6868/myapp/retrieve_from_sku?sku=E0F1G2H3

Retrieve available:

http://localhost:6868/myapp/retrieve_available

Retrieve sold out:

http://localhost:6868/myapp/retrieve_sold_out

## Consideration

Six hours were taken to implement this solution instead of three
