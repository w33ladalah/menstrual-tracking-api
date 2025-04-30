# Menstrual Cycle Tracking Application

## About This Project

I created this application to help my daughter monitor and track her menstrual cycles in a safe, private, and empowering way. As a parent, I wanted to provide her with a tool that would:

- Help her understand her body better
- Track her cycles reliably
- Give her more confidence in managing her menstrual health
- Provide helpful insights and predictions
- Maintain her privacy and data security

## Features

- Secure user accounts and data privacy
- Period tracking and cycle predictions
- Symptom and mood logging
- Customizable reminders and notifications
- Health insights and cycle analytics
- Educational resources about menstrual health
- Mobile-friendly interface

## Technical Stack

### Backend
- FastAPI (Python web framework)
- SQLAlchemy for database operations
- PostgreSQL database
- Redis for caching
- JWT authentication
- RESTful API design
- Alembic for database migrations

### Frontend
- React.js
- Material-UI components
- Responsive design
- Progressive Web App (PWA) capabilities

## Getting Started

### Prerequisites
- Python 3.8+
- Docker and Docker Compose (recommended for easy setup)
- PostgreSQL (if running without Docker)
- Redis (if running without Docker)

### Installation and Setup

#### Using Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd menstrual-tracking/backend
   ```

2. Start the application using Docker Compose:
   ```bash
   docker-compose up -d
   ```

3. The API will be available at `http://localhost:8000`
   - API documentation: `http://localhost:8000/docs`
   - Database admin interface: `http://localhost:8088`

#### Manual Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd menstrual-tracking/backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (create a `.env` file in the root directory):
   ```
   ENVIRONMENT=development
   POSTGRES_SERVER=localhost
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=menstrual_tracking
   POSTGRES_PORT=5432
   REDIS_HOST=localhost
   REDIS_PORT=6379
   REDIS_DB=0
   SECRET_KEY=your-secret-key-change-in-production
   ```

5. Run database migrations:
   ```bash
   alembic upgrade head
   ```

6. Start the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Documentation

After starting the application, you can access the interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Authentication

The API uses JWT (JSON Web Token) authentication to secure endpoints. To access protected endpoints:

1. Register a user account using the `/api/v1/auth/register` endpoint
2. Obtain a JWT token by sending a POST request to `/api/v1/auth/login` with your credentials
3. Include the token in the `Authorization` header of your requests: `Bearer <your_token>`

Most content endpoints are protected and require authentication, except for the public educational resources endpoint (`/api/v1/content/public/educational`), which is accessible without authentication.

Example authentication flow:

```bash
# Register a new user
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "username": "testuser", "password": "securepassword"}'

# Login to get token
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=securepassword"

# Access protected endpoint with token
curl -X GET "http://localhost:8000/api/v1/content/content" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

# Access public educational content (no authentication required)
curl -X GET "http://localhost:8000/api/v1/content/public/educational"
```

## Development

### Running Tests
Coming soon

### Database Migrations

The application uses Alembic for database migrations, which is configured to read settings from the `.env` file.

To create a new migration after changing models:
```bash
alembic revision --autogenerate -m "Description of changes"
alembic upgrade head
```

#### How Environment Variables Work with Alembic
- Environment variables are loaded from the `.env` file using Pydantic Settings
- Alembic's `env.py` script imports the settings and dynamically configures the database URL
- This ensures consistency between your application and migration settings

## License
Coming soon
