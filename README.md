# sendIT

[![Build Status](https://travis-ci.com/dorothyas/sendIT.svg?branch=develop)](https://travis-ci.com/dorothyas/sendIT)
[![Coverage Status](https://coveralls.io/repos/github/dorothyas/sendIT/badge.svg?branch=develop)](https://coveralls.io/github/dorothyas/sendIT?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/e050bb8dd42c1f2d6594/maintainability)](https://codeclimate.com/github/dorothyas/sendIT/maintainability)

SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.

### API endpoints

- Register a user
- Login a user
- Create a parcel delivery order
- Fetch all parcel delivery orders
- Fetch a specific parcel delivery order
- Change the status of a specific parcel delivery order
- Change the present location of a specific parcel delivery order
- Create a parcel delivery order

## Built with
- Python 3

## Prerequisites
- GIT

    • to update and clone the repository
    ``` 
    $ git clone
    ```
- IDE e.g Visual Studio Code
- Postman

### Activate virtual enviroment
    ``` 
    $  venv venv
     source /env/bin/activate

    ```
### Install dependencies
    ``` 
    $ pip install -r requirements.txt

    ```
### Running Tests
• To run tests, use the command below;
    ``` 
    $ pytest

    ```
### Run server
    ``` 
    $ python run.py
    ```

## Endpoints

|Endpoint |Functionality |
|---------|:------------:|
|POST /auth/signup|Register a user| 
|POST /auth/login|Login a user| 
|GET /parcels|Fetch all parcel delivery orders| 
|GET /parcels/<parcelId>|Fetch a specific parcel delivery order|
|PUT /parcels/<parcelId>/status |Change the status of a specific parcel delivery order|
|PUT /parcels/<parcelId>/presentLocation|Change the present location of a specific parcel delivery order|
|PUT /parcels/<parcelId>/destination| Change the location of a specific parcel delivery order| 

## Project links:
•	Github Pages: https://dorothyas.github.io/send_IT/UI

• Heroku : https://stargal-dorothy.herokuapp.com/api/v1/parcels
## Author
- Dorothy Asiimwe
