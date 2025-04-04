# Project Structure

## Root Directory Structure
```
haven-sync-backend/
├── authentication/             # Authentication app
│   ├── api/                    # API endpoints
│   │   └── v1/                 # API version 1
│   │       ├── serializers.py
│   │       ├── urls.py
│   │       └── views.py
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py           # User model
│   ├── tests.py
│   └── views.py
│
├── docs/                       # Documentation
│   └── authentication/         # Auth module docs
│       ├── api_docs.md         # API documentation
│       └── architecture.md     # Architecture details
│
├── hexa_haven/             # Project settings
│   ├── __init__.py
│   ├── asgi.py            # ASGI configuration
│   ├── settings.py        # Project settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
│
├── media/                  # User uploaded files
│  
│
├── staticfiles/           # Collected static files
│
├── .env                   # Environment variables
├── .gitignore            # Git ignore rules
├── manage.py             # Django management script
├── project_structure.md  # This file
└── README.md             # Project documentation
```

## Key Directories

### Authentication App
The `authentication/` directory contains all authentication-related code:
- User model definition
- API endpoints for auth operations
- Serializers for data validation
- URL routing for auth endpoints

### Documentation
The `docs/` directory contains detailed documentation:
- API specifications
- Architecture diagrams
- Authentication flows
- Implementation details

### Project Configuration
The `hexa_haven/` directory contains project-level settings:
- Django settings
- URL configurations
- WSGI/ASGI configurations

### Media and Static Files
- `media/`: User-uploaded content
- `staticfiles/`: Collected static files for production

### Configuration Files
- `.env`: Environment-specific settings
- `.gitignore`: Git ignore patterns
- `manage.py`: Django CLI tool
- `README.md`: Project overview and setup guide
