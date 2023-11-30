## Django REST Framework (Full Warehouse API)

## Overview

This is a comprehensive REST API Django project that provides a robust warehouse and product management system. It is currently in the final stages of testing and is nearing completion. The project boasts a rich feature set designed to handle various aspects of warehouse operations and product management.

## Features

Here some of the features that include this REST API:

- **JWT Authentication System**: Employs a secure and industry-standard JSON Web Tokens (JWT) authentication mechanism to protect user access.

- **Role-Based Authorization System**: Implements a granular role-based authorization system to control user access and permissions based on their designated roles.

- **Area and Location Management**: Provides functionality to manage and organize warehouse areas and locations for efficient product storage and tracking.

- **Order and Customer Management**: Facilitates order processing, customer management, and order fulfillment capabilities.

- **Environment-Specific Settings**: Allows for configuration and customization of settings for different environments, ensuring seamless deployment across various setups.

## Create a super user

You can access to the admin panel to test the project, you can create a super user to do it with the following command.

```bash
python3 manage.py createsuperuser
```

## Using Virtualenv

1. Create a virtual environment using:

```bash
python3 -m venv .venv
```

2. Activate the virtual environment:

```bash
source .venv/bin/active
```

3. Install project dependencies:

```bash
pip3 install -r requirements.txt
```

4. Apply database migrations:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

5. Run the Django development server:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## Run with docker

**Important**: Docker is not setup for completed, use Using Virtualenv instead.

Build and run the Docker containers:

```bash
sudo docker-compose up
```

## Project Usage

Once the project is installed and running, you can access the API documentation and interact with the API endpoints using tools like Postman or curl. Refer to the project documentation for detailed instructions on API usage and specific endpoint functionalities.
