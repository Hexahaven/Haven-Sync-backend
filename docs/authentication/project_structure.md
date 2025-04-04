# Authentication Project Structure

## Directory Structure
```
authentication/
├── api/
│   └── v1/
│       ├── __init__.py
│       ├── serializers.py      # Request/Response data serialization
│       ├── urls.py            # API endpoint routing
│       └── views.py           # API view logic
├── migrations/
├── __init__.py
├── admin.py                   # Django admin configuration
├── apps.py                    # App configuration
├── models.py                  # User model definition
├── tests.py                   # Unit tests
└── views.py                   # Web views (if any)
```

## Key Components

### Models
- `User` - Custom user model extending Django's AbstractUser
- `CustomUserManager` - Custom manager for User model operations

### API Components
- **Serializers**: Handle data validation and transformation
  - `SignupSerializer`
  - `SigninSerializer`

- **Views**: Handle API logic
  - `SignupView`
  - `SigninView`
  - `TokenRefreshView` (from SimpleJWT)

- **URLs**: Define API endpoints
  - `/signup/`
  - `/signin/`
  - `/token/refresh/`
