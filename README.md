# FinTrack API

FinTrack API is a production-grade backend system built using FastAPI for managing financial records. It includes authentication, role-based access control, analytics, caching, rate limiting, validation, and structured error handling.

---

## Overview

This project demonstrates a scalable backend architecture with clean separation of concerns and industry-standard practices. It is designed to handle financial record management with secure access and optimized performance.

---

## Features

### Authentication and Authorization
- JWT-based authentication
- Secure password hashing using bcrypt
- Protected routes
- Role-Based Access Control (RBAC)

### Roles
- Viewer: Read-only access
- Analyst: Access to records and analytics
- Admin: Full access including creation and management

---

### Financial Records
- Create financial records (income and expense)
- Retrieve records with filtering and pagination
- Structured service-based logic

---

### Dashboard and Analytics
- Total income and expense
- Net balance calculation
- Category-wise aggregation
- Category grouped by transaction type

---

### Performance Enhancements
- Redis caching for dashboard endpoints
- Cache invalidation on data updates
- Rate limiting using SlowAPI

---

### Validation and Error Handling
- Input validation using Pydantic
- Business logic validation at service layer
- Centralized exception handling
- Consistent error response format

---

### Architecture

The project follows a layered architecture:

- models: Database models
- schemas: Request and response validation
- services: Business logic
- api: Route definitions
- core: Configuration, security, and utilities

---

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Redis
- Python-JOSE (JWT)
- Passlib (bcrypt)
- SlowAPI

---

## Project Structure
app/
api/
v1/
endpoints/
core/
db/
models/
schemas/
services/
cache/



---

## Setup Instructions

### Clone Repository
git clone https://github.com/your-username/fintrack-api.git
cd fintrack-api


---

### Create Virtual Environment
python -m venv venv
venv\Scripts\activate


---

### Install Dependencies
pip install -r requirements.txt


---

### Environment Variables

Create a `.env` file in the root directory:
DATABASE_URL=postgresql://postgres:password@localhost:5432/fintrack
SECRET_KEY=your_secret_key

### Run Server
uvicorn main:app --reload


---

## Rate Limiting

- Applied per client
- Example: 5 requests per minute

---

## Caching

- Redis used for dashboard endpoints
- Cache invalidated on record creation/update

---

## Design Decisions

- Service layer for business logic separation
- Dependency injection for DB/session handling
- Stateless authentication using JWT
- Redis for performance optimization
- Centralized error handling

---

## Future Improvements

- Docker support
- CI/CD pipeline
- Async database support
- Background jobs
- Monitoring and logging

---

## Author

This project demonstrates backend engineering practices including scalability, security, performance optimization, and clean architecture.