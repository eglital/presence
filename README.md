# Github issue viewer

This is a web application that allows users to view Github issues for a specified repository (currently hardcoded to view VSCode repo only). The backend is built with Python, Django, and Django Rest Framework, while the frontend is built with React.

# Getting started

These instructions will help you get a copy of the project up and running on your local machine for testing and development purposes.

# Prerequisities

Docker
Docker Compose

# Installing

1. Clone the repository.
2. In the root directory of the project, run the following command to start the Docker containers:
   `docker-compose up --build`
3. The frontend should now be accessible in your web browser at http://localhost:3000, and the backend API should be accessible at http://localhost:8000/api

# Usage

Currently frontend is hardcoded to only show Microsoft/VSCode repository issues.
It could be expanded to include a search box, that would allow to enter the owner and the name of the repo in the search bar, and display the found issues. Backend API endpoint is already setup to accept owner and name as query params.

# Built With

- Python
- Django
- Django Rest Framework
- React
