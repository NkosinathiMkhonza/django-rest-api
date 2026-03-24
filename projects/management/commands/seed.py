from django.core.management.base import BaseCommand
from projects.models import Project


class Command(BaseCommand):
    help = 'Seed the database with initial project data'

    def handle(self, *args, **kwargs):
        if Project.objects.exists():
            self.stdout.write('Database already seeded. Skipping.')
            return

        projects = [
            {
                'title': 'task-manager-cli',
                'description': 'A command-line task manager built with Python and SQLite, extended with a Flask REST API and terminal-style web interface.',
                'tech_stack': 'Python, SQLite, Flask',
                'status': 'completed',
                'github_url': 'https://github.com/NkosinathiMkhonza/task-manager-cli',
            },
            {
                'title': 'django-rest-api',
                'description': 'A REST API built with Django REST Framework featuring CRUD operations, model serialization, and a browsable API interface.',
                'tech_stack': 'Python, Django, Django REST Framework',
                'status': 'active',
                'github_url': 'https://github.com/NkosinathiMkhonza/django-rest-api',
            },
            {
                'title': 'portfolio',
                'description': 'A documentation-style developer portfolio with Bootstrap grid layout, live GitHub commit feed, and terminal-style contact form.',
                'tech_stack': 'HTML, CSS, JavaScript, Bootstrap',
                'status': 'active',
                'github_url': 'https://github.com/NkosinathiMkhonza/Portfolio',
            },
        ]

        for p in projects:
            Project.objects.create(**p)
            self.stdout.write(f'Created: {p["title"]}')

        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))