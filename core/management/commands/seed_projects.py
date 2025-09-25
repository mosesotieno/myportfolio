from django.core.management.base import BaseCommand
from django.utils.text import slugify
from core.models import Project
from taggit.models import Tag
from datetime import date

class Command(BaseCommand):
    help = "Seed initial featured projects into the database"

    def handle(self, *args, **kwargs):
        projects = [
            {
                "title": "EAPoC-VL Project",
                "short_description": "Point of Care HIV Viral Load Monitoring for Children and Adolescents in East Africa",
                "description": "A study focusing on improving access to HIV viral load monitoring...",
                "project_type": "other",
                "icon_class": "fas fa-virus fa-3x",
                "background_class": "bg-primary",
                "start_date": date(2025, 2, 1),
                "end_date": None,
                "featured": True,
                "order": 1,
                "technologies": ["R", "Python", "SQL Server"],
            },
            {
                "title": "Climate & Wearables",
                "short_description": "Assessing Climate Change Impact on Malaria and HIV using Wearable Technology",
                "description": "An exploratory project leveraging wearable sensors and climate data...",
                "project_type": "other",
                "icon_class": "fas fa-cloud-sun fa-3x",
                "background_class": "bg-success",
                "start_date": date(2024, 10, 1),
                "end_date": date(2024, 11, 30),
                "featured": True,
                "order": 2,
                "technologies": ["Python", "R", "Machine Learning"],
            },
            {
                "title": "DREAMS Partnership",
                "short_description": "HIV Prevention for Adolescent Girls and Young Women in Kenya and South Africa",
                "description": "Evaluation of DREAMS program focusing on adolescent HIV prevention...",
                "project_type": "other",
                "icon_class": "fas fa-female fa-3x",
                "background_class": "bg-warning",
                "start_date": date(2023, 2, 1),
                "end_date": date(2024, 9, 30),
                "featured": True,
                "order": 3,
                "technologies": ["Statistical Analysis", "Data Management", "Survey Solutions"],
            },
        ]

        for data in projects:
            project, created = Project.objects.update_or_create(
                slug=slugify(data["title"]),
                defaults={
                    "title": data["title"],
                    "short_description": data["short_description"],
                    "description": data["description"],
                    "project_type": data["project_type"],
                    "icon_class": data["icon_class"],
                    "background_class": data["background_class"],
                    "start_date": data["start_date"],
                    "end_date": data["end_date"],
                    "featured": data["featured"],
                    "order": data["order"],
                },
            )

            # Assign technologies
            project.technologies_used.set(
                [Tag.objects.get_or_create(name=tech)[0] for tech in data["technologies"]]
            )
            project.save()

            if created:
                self.stdout.write(self.style.SUCCESS(f"Created project: {project.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Updated project: {project.title}"))

        self.stdout.write(self.style.SUCCESS("✅ Projects seeded successfully!"))
