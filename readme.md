# User Resource CRUD application

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.3-blue)
![MongoDB](https://img.shields.io/badge/MongoDB-6.0-green)


This is a CRUD application that allows users to create, read, update and delete users. It is designed to be highly scalable and reliable.

## Installation

To install the application, follow these steps:

1. Clone the repository

```bash
git clone https://github.com/RohanKhatua/corider-assignment.git
```

2. Change into the project directory

```bash
cd corider-assignment
```

3. Set up the environment variables

```bash
cp .env.example .env
```

Edit the `.env` file and set the environment variables as required.

4. Use docker-compose to build the application

```bash
docker-compose up --build -d
```

5. The application should now be running on `http://localhost:6000`

## API Documentation

The API documentation can be found [here](https://www.postman.com/solar-robot-552906/my-public-workspace/request/o4xkaxx/create-user)

## Tech Stack

- Flask
- MongoDB
- Docker
- Postman (for API testing)

## Features

- Uses Gunicorn as the WSGI server, which is highly scalable and reliable. Also acts as a load balancer for multiple worker processes. Incoming requests are distributed among the worker processes.

- Uses MongoDB as the database, which is a NoSQL database and is highly scalable and reliable. In order to increase performance, we have created read 2 replicas of the database along with a primary instance.

- Implements a cursor-based pagination system to handle a large number of users in the get all users endpoint.

- Uses Docker compose to build and run the applicaton as well as the MongoDB instances.

## Future Improvements

- Implement a caching layer to cache the responses of the get all users endpoint if the data is not updated frequently.

- Implement a rate limiting system to prevent abuse of the API.

- Implement a queue system to decouple the API from the database and handle a large number of requests efficiently.
---

Made with ❤️ by [Rohan Khatua](https://github.com/RohanKhatua)

