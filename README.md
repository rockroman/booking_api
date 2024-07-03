# Booking System API

## Overview

This Django-based project implements a Booking System API using Django REST Framework (DRF). It allows users to manage services, time slots, and bookings for various services.

## Requirements

- Python Python 3.11.6
- Django 4.2
- Django REST Framework 3.15.2

## Installation

1. **Clone the repository:**

   ```
   git clone <repository_url>
   cd simple_booking_drf
   ```

### Setup virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies:

```
pip install -r requirements.txt
```

### Database migrations:

```
python manage.py migrate
```

### Create a superuser (admin):

```
python manage.py createsuperuser
```

### Run the development server:

```
python manage.py runserver

```

# Usage

## Accessing Services:

Use `/services/` endpoint to manage services.

- Create, update, delete services via API.(ADMIN user only)

## Managing Time Slots:

There is no endpoint to manage time slots.
that functionality is strictly ADMIN related

- Create, update, delete time slots associated with services.
  (to create timeslot for service start_time field is required while
  end_time is calculated based on service duration field)

## Making Bookings:

Use `/bookings/` endpoint to create bookings.

- Select a service and available time slot for booking.

## Admin Interface:

Access Django Admin at `/admin/` to manage models interactively.

- Manage users, services, time slots, and bookings.
