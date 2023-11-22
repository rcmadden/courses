# Course Notes and Observations
## API
connects the backend to the front end
Sits on the backend as a connector between the front end and backend (app application  data)

## REST 
an architectural pattern

What is un-restful?

## Pydantic models
In a model you can use another model as a type hint

Mock database
json file

## generate secret key
from python cli
import os
os.urandom(24).hex()

## explore secure authorization
fastapi-login - barebones and customizable
fasapti-users - ready-to-use register, login, reset password and verify e-mail routes, customizable (database/auth) backend & more

## alembic commands
for migrating and upgrading database
alembic init alembic
alembic revision --autogenerate -m 'First revision'
alembic init alembic
