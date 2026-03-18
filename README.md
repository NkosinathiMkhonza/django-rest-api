# django-rest-api

A REST API built with Django REST Framework featuring CRUD operations, model serialization, and a browsable API interface.

---

## Features

- Full CRUD operations on Projects
- Django REST Framework browsable API
- Model serialization with validation
- Project stats endpoint
- Django admin panel for data management
- SQLite database

---

## Requirements

- Python 3.8+
- Django
- Django REST Framework

---

## Installation
```bash
git clone https://github.com/NkosinathiMkhonza/django-rest-api.git
cd django-rest-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/projects/` | List all projects |
| POST | `/api/v1/projects/` | Create a project |
| GET | `/api/v1/projects/<id>/` | Get a project |
| PUT | `/api/v1/projects/<id>/` | Update a project |
| DELETE | `/api/v1/projects/<id>/` | Delete a project |
| GET | `/api/v1/projects/stats/` | Get project stats |

---

## Example Response
```json
{
    "id": 1,
    "title": "task-manager-cli",
    "description": "A command-line task manager...",
    "tech_stack": "Python, SQLite, Flask",
    "status": "completed",
    "github_url": "https://github.com/NkosinathiMkhonza/task-manager-cli",
    "created_at": "2026-03-18T09:00:00Z",
    "updated_at": "2026-03-18T09:00:00Z"
}
```

---

## Project Structure
```
django-rest-api/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── projects/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## Author

**Nkosinathi Mkhonza** — [github.com/NkosinathiMkhonza](https://github.com/NkosinathiMkhonza)