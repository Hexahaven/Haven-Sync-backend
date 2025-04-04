# Authentication API Documentation

## Base URL
```
http://localhost:8000/api/v1/auth/
```

## Endpoints

### 1. Sign Up
Create a new user account.

**Endpoint:** `POST /signup/`

**Request Body:**
```json
{
    "full_name": "John Doe",
    "email": "john@example.com",
    "password": "secure_password123"
}
```

**Response (201 Created):**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "user": {
        "id": 1,
        "full_name": "John Doe",
        "email": "john@example.com"
    }
}
```

**Validation Rules:**
- Full name: 3-50 characters, letters and spaces only
- Email: Valid email format, unique
- Password: Django's default password validation

### 2. Sign In
Authenticate existing user.

**Endpoint:** `POST /signin/`

**Request Body:**
```json
{
    "email": "john@example.com",
    "password": "secure_password123"
}
```

**Response (200 OK):**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "user": {
        "id": 1,
        "full_name": "John Doe",
        "email": "john@example.com"
    }
}
```

### 3. Refresh Token
Get new access token using refresh token.

**Endpoint:** `POST /token/refresh/`

**Request Body:**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Response (200 OK):**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

## Error Responses

### 400 Bad Request
```json
{
    "field_name": [
        "Error message"
    ]
}
```

### 401 Unauthorized
```json
{
    "error": "Invalid credentials"
}
```

### 403 Forbidden
```json
{
    "detail": "Authentication credentials were not provided."
}
```

## Authentication

All protected endpoints require a JWT token in the Authorization header:
```
Authorization: Bearer <access_token>
```

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error