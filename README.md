# FastAPI Project

This project is a FastAPI application with various features including user authentication, article management, and more.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/fast-back.git
    cd fast-back
    ```

2. Create a `.env` file in the root directory and add the necessary environment variables:
    ```env
    SECRET_KEY=your_secret_key
    REFRESH_SECRET_KEY=your_refresh_secret_key
    DATABASE_URL=postgresql://postgres:postgres@db/postgres
    ```

3. Build and start the Docker containers:
    ```bash
    docker-compose up --build
    ```

4. The application will be available at `http://localhost:8000`.

## File Structure

```
fast-back/
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── api.py                # Main API router
│   │   │   ├── authentication.py     # Authentication routes
│   │   │   ├── health_check.py       # Health check route
│   │   │   ├── users.py              # User-related routes
│   │   │   ├── profiles.py           # Profile-related routes
│   │   │   ├── comments.py           # Comment-related routes
│   │   │   ├── tags.py               # Tag-related routes
│   │   │   └── articles/
│   │   │       └── api.py            # Article-related routes
│   ├── core/
│   │   ├── config.py                 # Configuration settings
│   │   └── security.py               # Security utilities (e.g., token creation)
│   ├── db/
│   │   ├── repositories/
│   │   │   ├── articles.py           # Article repository
│   │   │   ├── base.py               # Base repository
│   │   │   ├── profiles.py           # Profile repository
│   │   │   └── tags.py               # Tag repository
│   │   └── errors.py                 # Database-related errors
│   ├── models/
│   │   ├── domain/
│   │   │   ├── articles.py           # Article domain model
│   │   │   ├── users.py              # User domain model
│   │   └── token.py                  # Token model
│   └── main.py                       # Application entry point
├── docker-compose.yml                # Docker Compose configuration
└── README.md                         # Project documentation
```

## Features

- User authentication with JWT tokens
- Refresh token support
- Article management (CRUD operations)
- Comment management
- Tag management
- User profiles
- Health check endpoint

## Technologies Used

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **PostgreSQL**: A powerful, open-source object-relational database system.
- **Docker**: A platform for developing, shipping, and running applications in containers.
- **Adminer**: A full-featured database management tool written in PHP.

## Packages Used

- **fastapi**: The main framework used to build the API.
- **asyncpg**: An asynchronous PostgreSQL client library for Python.
- **pydantic**: Data validation and settings management using Python type annotations.
- **jose**: A JavaScript Object Signing and Encryption (JOSE) implementation in Python.
- **passlib**: A comprehensive password hashing framework supporting over 30 schemes.
- **uvicorn**: A lightning-fast ASGI server implementation, using `uvloop` and `httptools`.

## API Endpoints

### Authentication

- `POST /users/login`: Login and get access and refresh tokens.
- `POST /token/refresh`: Refresh the access token using a refresh token.

### Users

- `GET /user`: Get the current user's profile.
- `POST /users`: Register a new user.

### Articles

- `GET /articles`: Get a list of articles.
- `POST /articles`: Create a new article.
- `GET /articles/{slug}`: Get an article by slug.
- `PUT /articles/{slug}`: Update an article by slug.
- `DELETE /articles/{slug}`: Delete an article by slug.

### Profiles

- `GET /profiles/{username}`: Get a user's profile by username.

### Comments

- `GET /articles/{slug}/comments`: Get comments for an article.
- `POST /articles/{slug}/comments`: Add a comment to an article.
- `DELETE /articles/{slug}/comments/{id}`: Delete a comment from an article.

### Tags

- `GET /tags`: Get a list of tags.

## Database

The application uses PostgreSQL as the database. The database service is defined in the `docker-compose.yml` file.

## Adminer

Adminer is included for database management. It will be available at `http://localhost:8080`.

## License

This project is licensed under the MIT License.
