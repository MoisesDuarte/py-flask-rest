# Python + Flask Rest API

## Setup
- To create the sqlite database, run in python shell:
  - from app import db
  - db.create_all()
- From default shell, run:
  - pipenv install
  - pipenv shell
  - py app.py


## Endpoints
- CREATE PRODUCT
  - **Route:** /product
  - **Method:** POST
  - **Payload**: { name: String, description: String, price: Float, qty: Integer }

- UPDATE PRODUCT
  - **Route:** /product/<id>
  - **Method:** PUT
  - **Payload**: { name: String, description: String, price: Float, qty: Integer }

- DELETE PRODUCT
  - **Route:** /product/<id>
  - **Method:** DELETE
  - **Payload**: NONE

- GET ALL PRODUCT
  - **Route:** /product
  - **Method:** GET
  - **Payload**: NONE

- GET SINGLE PRODUCT
  - **Route:** /product/<id>
  - **Method:** GET
  - **Payload**: NONE

## Dependencies
- Python 3^
- Pipenv
- Flask
- SQLAlchemy
- Marshmallow