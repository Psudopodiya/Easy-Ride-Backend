
# Easy Ride Backend

Easy Ride is a car rental service that allows users to book cars, view available car listings, and manage their bookings. This repository contains the backend API built using Django and Django REST Framework, with JWT-based authentication.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Register, login, and manage user accounts using JWT.
- **Car Listings**: View available cars and filter them by brands.
- **Booking Management**: Book cars, view user-specific bookings, and calculate booking costs.

## Tech Stack

- **Django**: Backend framework for building web applications.
- **Django REST Framework**: Toolkit for building Web APIs.
- **JWT (JSON Web Tokens)**: For securing API endpoints.

## Installation

### Prerequisites

- Python 3.8+
- Django 3.x or 4.x
- PostgreSQL (optional, can use SQLite for local development)

### Clone the Repository

```bash
git clone https://github.com/yourusername/easy-ride-backend.git
cd easy-ride-backend
```

### Install Dependencies

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Migrate Database

Run migrations to set up the database schema:

```bash
python manage.py migrate
```

### Create a Superuser

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

### Run the Development Server

Start the server locally:

```bash
python manage.py runserver
```

The server will be running at `http://localhost:8000/`.

## Environment Variables

Create a `.env` file in the root directory to configure environment variables. Below is an example configuration:

```env
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:password@localhost:5432/easy_ride_db
```

- **DEBUG**: Set to `False` in production.
- **SECRET_KEY**: A secret key for a particular Django installation.
- **DATABASE_URL**: URL for the PostgreSQL database. If using SQLite, this can be omitted.

## Usage

### Authentication

1. **Register a New User**:

   ```
   POST /api/user/register/
   ```

2. **Login**:

   ```
   POST /api/login/
   ```

3. **Refresh Token**:

   ```
   POST /api/token/refresh/
   ```

### Car Listings

1. **Get Random Car List**:

   ```
   GET /api/cars/
   ```

2. **Get All Cars**:

   ```
   POST /api/cars/all-car-list/
   ```

3. **Get Car Details**:

   ```
   GET /api/cars/<int:pk>/
   ```

4. **Get Car Brands**:

   ```
   GET /api/cars/brands/
   ```

### Bookings

1. **Create a Booking**:

   ```
   POST /api/bookings/
   ```

2. **Get User Bookings**:

   ```
   GET /api/bookings/user/
   ```

## API Endpoints

Here's a summary of the available API endpoints:

### Authentication

- `POST /api/login/`: Obtain JWT tokens.
- `POST /api/token/refresh/`: Refresh JWT token.

### Users

- `POST /api/user/register/`: Register a new user.
- `GET /api/user/me/`: Get details of the logged-in user.

### Cars

- `GET /api/cars/`: Get a random list of cars.
- `POST /api/cars/all-car-list/`: Get a filtered list of cars.
- `GET /api/cars/<int:pk>/`: Get details of a specific car.
- `GET /api/cars/brands/`: Get a list of all car brands.

### Bookings

- `POST /api/bookings/`: Create a new booking.
- `GET /api/bookings/user/`: Get bookings of the logged-in user.

## Project Structure

```
easy-ride-backend/
│
├── cars/                   # Car-related models, views, serializers, and URLs
├── bookings/               # Booking-related models, views, serializers, and URLs
├── users/                  # User-related models, views, serializers, and URLs
├── Easy_Ride_Backend/      # Main project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL routing for the entire project
│   └── wsgi.py             # WSGI configuration for deployment
├── manage.py               # Django management script
├── .env.example            # Example environment configuration
└── README.md               # This README file
```

## Contributing

We welcome contributions to this project! To contribute:

1. Fork the repository.
2. Create a new feature branch.
3. Make your changes.
4. Submit a pull request.

Please ensure your code follows the project's coding standards and is well-documented.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
