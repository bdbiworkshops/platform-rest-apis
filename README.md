About
-
This repository contains source code for a BDBI @ Georgia Tech workshop that covers REST APIs.

Installation
-
1. Make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
2. Clone the repository with `git clone https://github.com/nathanaeng/bdbi-rest-api`
3. Build the application with `docker-compose up --build`
4. Navigate to http://localhost:8080 to view the website

Architecture
-
This multi-container application is made up of 3 containers:
1. app: an nginx web server that hosts a static website and serves as a reverse proxy to the Flask application
2. python_app: a REST API written in Flask used to communicate with the PostgreSQL database
3. db: a PostgreSQL database