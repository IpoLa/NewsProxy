NewsProxy
Overview
NewsProxy is a web application designed to aggregate news articles from various sources and provide users with a centralized platform to browse and search for news based on their preferences.

Features
News Aggregation: Fetches news articles from multiple sources and categories.
Search Functionality: Allows users to search for articles based on keywords.
Filtering: Provides filtering options by category, source, country ...
Responsive Design: Optimized for desktop and mobile devices.
Technologies Used
Backend: Django framework with Django REST Framework for API development.
Frontend: Angular framework for building the user interface.
Database: PostgreSQL for storing news articles, user data, and preferences.
Celery: Used for task scheduling and background job processing.
Swagger/OpenAPI: API documentation using Swagger UI.
Docker: Containerization for easy deployment and scalability.
Getting Started
Clone the repository: git clone https://github.com/IpoLa/NewsProxy.git
Navigate to the project directory: cd NewsProxy
Install dependencies:
Backend: pip install -r requirements.txt
Frontend: npm install
Set up the database:
Run migrations: python manage.py migrate
Start the development server:
Backend: python manage.py runserver
Frontend: ng serve
Access the application in your browser: http://localhost:8000
Configuration
Environment Variables: Configure environment variables for sensitive information such as API keys, database credentials, etc.
Settings: Adjust settings in settings.py for customization and production deployment.
