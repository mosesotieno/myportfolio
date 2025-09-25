# core/management/commands/specialize_seed.py
from django.core.management.base import BaseCommand
from core.models import Specialization

class Command(BaseCommand):
    help = "Seed the database with default specializations"

    def handle(self, *args, **kwargs):
        data = [
            {
                "title": "HIV/AIDS Research",
                "description": "Advanced statistical analysis and data management for HIV prevention and treatment studies",
                "icon_class": "fas fa-virus-slash fa-3x text-primary",
                "order": 1,
            },
            {
                "title": "Climate & Health",
                "description": "Studying the impact of climate change on disease patterns using wearable technology",
                "icon_class": "fas fa-temperature-high fa-3x text-success",
                "order": 2,
            },
            {
                "title": "Data Systems",
                "description": "Building robust data collection and management systems for large-scale research projects",
                "icon_class": "fas fa-database fa-3x text-info",
                "order": 3,
            },
        ]

        for item in data:
            spec, created = Specialization.objects.get_or_create(
                title=item["title"],
                defaults=item
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {spec.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Skipped (already exists): {spec.title}"))

        self.stdout.write(self.style.SUCCESS("Specializations seeding complete!"))
