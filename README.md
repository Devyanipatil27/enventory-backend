# Inventory System

### Main repository for Inventory System Project

![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

## Project Overview

The Inventory System is a backend application designed to manage and track inventory items efficiently. It is built using Django Rest Framework, PostgreSQL, Redis, and JWT for authentication. The application supports CRUD operations and utilizes caching to enhance performance.

## Project Requirements

- **API Framework**: Use Django Rest Framework (DRF) to create the API.
- **Database**: Use PostgreSQL to store inventory items.
- **Caching**: Use Redis to cache frequently accessed items.
- **Authentication**: Use JWT for securing the API endpoints.
- **Logging**: Integrate a logging system for debugging and monitoring.
- **Testing**: Implement unit tests using Django’s test framework to verify the functionality of the API.

## Database Configuration

Please configure your database with the following values in your `.env` file:

SECRET_KEY='vNi0tdc6PIVjVm1CbBWGymwzWRVHdo3G7OOnt9BhVa2UoVNzou8cRWAgRmO__0j86cM' 
DB_NAME='inventory_database' 
DB_USER='inventory_database'
DB_PASSWORD='inventory' 
DB_HOST='localhost' 
DB_PORT='5432' 
REDIS_URL='redis://localhost:6379/0'


## Commands for Project Setup

### Clone 

git clone https://github.com/Devyanipatil27/enventory-backend.git

### Navigate to the Project Directory

cd inventory_system

### Set Up a Virtual Environment

python -m venv .venv

### On Linux/MacOS:

source .venv/bin/activate

### On Windows:

.venv\Scripts\activate

### Install Required Dependencies

pip install -r requirements.txt

### Migrate the Database

python manage.py migrate

### Run the Project

python manage.py runserver

### Run Unit Tests

python manage.py test

## Git Commands

### Create a New Branch

git checkout -b <branch-name>

### Check Git Status

git status

### Stage Your Changes

git add .

### Commit Your Changes

git commit -m "Your commit message"

### Push Changes to the Remote Repository

git push origin <branch-name>

## Docker Setup

### Install Docker

Make sure Docker is installed on your system. You can download Docker from here.

###  Build the Docker Image

docker build -t inventory-system .

###  Run the Docker Container

docker run --env-file .env -p 8000:8000 inventory-system

###  Stop the Docker Container

docker stop $(docker ps -q)
docker rm $(docker ps -a -q)

###  Running with Docker Compose

docker-compose up --build

