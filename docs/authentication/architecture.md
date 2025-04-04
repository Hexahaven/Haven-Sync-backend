# Hexa Haven - Authentication Architecture Schema

## System Architecture Overview

```
┌────────────────────────────────────────────────────┐
│                           CLIENT LAYER             │
│                                                    │                  
│  ┌───────────────────┐                             │                   
│  │   User Interface  │                             │                 
│  │   (Web/Mobile)    │                             │              
│  └─────────┬─────────┘                             │                   
│            │                                       │               
└────────────┼───────────────────────────────────────┘
             │
             │ HTTP/HTTPS
             │
┌────────────┼───────────────────────────────────────────────────────────┐
│            │         AUTHENTICATION API LAYER                          │
│            ▼                                                           │
│  ┌───────────────────────────────────────────────────────────────┐     │
│  │                    Django REST Framework API                  │     │
│  │                                                               │     │
│  │  ┌─────────────┐   ┌─────────────┐   ┌─────────────────────┐  │     │
│  │  │ Sign Up API │   │ Sign In API │   │ Token Refresh API   │  │     │
│  │  └─────────────┘   └─────────────┘   └─────────────────────┘  │     │
│  └───────────────────────────────────────────────────────────────┘     │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
             │                      │                     │
             │                      │                     │
┌────────────┼──────────────────────┼─────────────────────┼─────────────┐
│            │     SERVICE LAYER                          │             │
│            ▼                      ▼                     ▼             │
│  ┌───────────────────┐  ┌───────────────────┐  ┌───────────────────┐  │
│  │  User Service     │  │  Auth Service     │  │  Token Service    │  │
│  └─────────┬─────────┘  └─────────┬─────────┘  └─────────┬─────────┘  │
│            │                      │                      │            │
└────────────┼──────────────────────┼──────────────────────┼────────────┘
             │                      │                      │
┌────────────┼──────────────────────┼──────────────────────┼─────────────┐
│            │     DATA LAYER                              │             │
│            ▼                      ▼                      ▼             │
│  ┌───────────────────┐  ┌───────────────────┐  ┌───────────────────┐   │
│  │ User Model        │  │ Token Blacklist   │  │ Token Store       │   │
│  │ (PostgreSQL)      │  │ (PostgreSQL)      │  │ (JWT)             │   │
│  └───────────────────┘  └───────────────────┘  └───────────────────┘   │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

## Component Interactions

### 1. Client-API Interaction
```
┌──────────┐     ┌───────────┐     ┌──────────────┐     ┌─────────────┐
│  Client  │────►│ API       │────►│ Serializer   │────►│ Database    │
│          │◄────│ Endpoint  │◄────│ Validation   │◄────│             │
└──────────┘     └───────────┘     └──────────────┘     └─────────────┘
```

### 2. Authentication Flow
```
┌──────────┐     ┌───────────┐     ┌──────────────┐     ┌─────────────┐
│  Client  │────►│ Sign In   │────►│ JWT Token    │────►│ Token       │
│          │◄────│ API       │◄────│ Generation   │◄────│ Blacklist   │
└──────────┘     └───────────┘     └──────────────┘     └─────────────┘
```

## Security Architecture

1. **Authentication Layer**
   - JWT-based authentication
   - Token refresh mechanism
   - Token blacklisting

2. **Data Protection**
   - Password hashing
   - Email validation
   - Input sanitization

3. **API Security**
   - Permission-based access
   - Rate limiting
   - CSRF protection

## Data Flow Diagrams

### Sign Up Process
```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Client  │───►│ Validate │───►│  Create  │───►│ Generate │
│  Request │    │  Input   │    │   User   │    │  Tokens  │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
```

### Sign In Process
```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Client  │───►│ Validate │───►│  Auth    │───►│ Generate │
│  Request │    │ Creds    │    │  User    │    │  Tokens  │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
```

## Database Schema

```
┌────────────────┐
│     User       │
├────────────────┤
│ id             │
│ full_name      │
│ email          │
│ password       │
│ is_active      │
│ is_staff       │
│ date_joined    │
└────────────────┘
       │
       │
┌──────▼─────────┐
│  TokenBlacklist│
├────────────────┤
│ id             │
│ token          │
│ blacklisted_at │
│ expires_at     │
└────────────────┘
```

## Technical Stack

1. **Backend Framework**
   - Django REST Framework
   - SimpleJWT for authentication

2. **Database**
   - PostgreSQL for user data
   - Token blacklist storage

3. **Security**
   - JWT tokens
   - Password hashing
   - Token rotation
