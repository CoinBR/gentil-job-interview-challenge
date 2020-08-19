# Gentil Job Interview Challenge

## Running the solution:

First, [Install Docker and Docker-Compose](https://www.techiediaries.com/ubuntu/install-docker-19-docker-compose-ubuntu-20-04/)
then:

     git clone https://github.com/CoinBR/gentil-job-interview-challenge.git
     cd gentil-job-interview-challenge/
     docker-compose up

## Using and Evaluating the solution:

### odoo app:

1. [http://localhost:8069/](http://localhost:8069/)
2.   email: **coinbr@gmail.com**
3.	 password: **senha**

### API consumer and provider:
[http://localhost:5000/](http://localhost:5000/)

## Understanding the Solution

### odoo / web-app

 - I was assigned to create a to-do list, using [odoo](https://www.odoo.com/) (OpenERP)
 - It should have many type of views
 - Also, I was asked to add a field "Mother name" to **res.partner**, and create appropriate views and inherited model
 - Also, It should be possible to assign a **task** to a **res.partner**

### API
- I should prove that I was able to
--	Access  the odoo api,
-- Authenticate on the odoo api
-- Consume **res.partner**s information, using the API

- So, I created my own simple REST Api:
-- It do all that was asked above (using python)
-- Gets a list off all partners that have the field "mother_name" filled 
-- Gets partner and mother names, for all partners found in the previous step 
-- Serve in my own simple REST API (using flask), the info gathered in the previous step, along with the partner id.

## Technologies used:
- [Python](https://www.python.org/)
- [Odoo (OpenERP)](https://www.odoo.com/)
- [XML](https://en.wikipedia.org/wiki/XML)
- [Docker](https://www.docker.com/) and [Docker-Compose](https://docs.docker.com/compose/)
- [Adminer](https://www.adminer.org/)
- [Flask](https://flask.palletsprojects.com/)
