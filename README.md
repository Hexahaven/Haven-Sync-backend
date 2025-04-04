# Haven Sync Backend

A Django-based backend for monitoring and controlling IoT devices.

## Features

- User Authentication with JWT
  - Sign up with full name, email, and password
  - Sign in with email and password
  - JWT token refresh functionality
  - Token blacklisting for security

## Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [git](https://git-scm.com/)

## Local Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hexa-haven.git
cd haven-sync-backend
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up PostgreSQL:
```sql
-- Run these commands in PostgreSQL shell (psql)
CREATE USER hexa_haven WITH PASSWORD 'hexa_haven';
CREATE DATABASE hexa_haven;
ALTER USER hexa_haven CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE hexa_haven TO hexa_haven;
```

5. Create `.env` file in the root folder and add the following content:
```env
SECRET_KEY=django-insecure-p&qfhkyp81wy5$#cy2c$@etq9wp&#gu_xy#pljome($$1rsdm8
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# Database Configuration
DB_ENGINE=django.db.backends.postgresql
DB_NAME=hexa_haven
DB_USER=hexa_haven
DB_PASSWORD=hexa_haven
DB_HOST=localhost
DB_PORT=5432
```

6. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Create superuser (optional):
```bash
python manage.py createsuperuser
```

8. Run development server:
```bash
python manage.py runserver
```

9. **Access the application**
  - Backend Server Running: http://localhost:8000/
  - Django inbuilt admin: http://localhost:8000/hexa-haven-admin/

## Documentation

The project documentation is located in the `docs` folder. To view the documentation:

1. Navigate to the `docs` folder:
```bash
cd docs/authentication
```

2. Open the following Markdown files in a Markdown viewer or editor:
   - `project_structure.md`: Provides an overview of the authentication module's structure.
   - `auth_flow.md`: Explains the authentication flow and system architecture.
   - `api_docs.md`: Contains detailed API documentation for authentication endpoints.
   - `architecture.md`: Describes the overall architecture of the authentication system.

You can use any Markdown viewer or editor, such as:
- Visual Studio Code
- Markdown Preview in your browser
- Command-line tools like `cat` or `less` for quick viewing
