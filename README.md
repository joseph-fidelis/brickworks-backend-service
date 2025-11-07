# Brickworks Backend Service

A Django-based backend service for Brickworks application.

## Prerequisites

- Python 3.9+
- PostgreSQL (or Docker for containerized database)
- Redis (optional, for Celery)

## Setup and Running (Docker Compose)

The easiest way to run the application is using Docker Compose:

```bash
# Clone the repository (if you haven't already)
git clone https://github.com/joseph-fidelis/brickworks-backend-service.git
cd brickworks-backend-service

# Build and start the containers
docker compose up --build
```

The application will be available at http://localhost:8000

## Local Development Setup

1. Create and activate a Python virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Database Setup:
   - Using Docker PostgreSQL (recommended):
     ```bash
     # PostgreSQL will be automatically started with docker-compose
     docker compose up postgres -d
     ```
   - The settings.py is already configured to connect to the Docker PostgreSQL instance

4. Run migrations:
```bash
python3 manage.py migrate
```

5. Create a superuser (optional):
```bash
python3 manage.py createsuperuser
```

6. Start the development server:
```bash
python3 manage.py runserver 0.0.0.0:8000
```

The application will be available at http://localhost:8000

## Additional Services

### Celery Workers (Optional)
If you need background task processing:

```bash
# Start Celery worker
celery -A brickwork_backend worker --loglevel=info

# Start Celery beat for scheduled tasks
celery -A brickwork_backend beat --loglevel=info
```

## Environment Variables

The application uses the following environment variables (already configured in Docker):

```env
POSTGRES_DB=zYgTABBA
POSTGRES_USER=uTvdPCAsJ2wUqwAYDE6b
POSTGRES_PASSWORD=HhXwsRg4+WHuC-@:1.wqfxCZKK1Tb-nad!WLjpiwkj^D+w
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

## Project Structure

```
brickworks-backend-service/
├── brickwork_backend/     # Main Django project settings
├── dashbaord/            # Dashboard application
├── data/                 # Data files and media
├── src/                  # Core business logic
├── static/              # Static files
├── templates/           # HTML templates
└── manage.py           # Django management script
```

## API Documentation

The API endpoints will be documented here (add your API documentation).

## Testing

To run the test suite:

```bash
python manage.py test
```

## Troubleshooting

1. Database Connection Issues:
   - Ensure PostgreSQL container is running: `docker ps | grep postgres`
   - Check database credentials in settings.py
   - Verify port 5432 is not in use by another service

2. Static Files:
   - Run `python manage.py collectstatic` if static files are not loading

3. Migrations:
   - For migration issues, try: `python manage.py migrate --run-syncdb`

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.