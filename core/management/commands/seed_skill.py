# core/management/commands/seed_skills.py
from django.core.management.base import BaseCommand
from core.models import SkillCategory, Skill

class Command(BaseCommand):
    help = "Seed default skills"

    def handle(self, *args, **kwargs):
        # Data Science Category
        ds, _ = SkillCategory.objects.get_or_create(
            name="Data Science & Statistics",
            icon_class="fas fa-chart-bar",
            order=1
        )
        Skill.objects.get_or_create(category=ds, name="Advanced Statistical Analysis", proficiency=95, color_class="bg-primary", order=1)
        Skill.objects.get_or_create(category=ds, name="R Programming", proficiency=90, color_class="bg-primary", order=2)
        Skill.objects.get_or_create(category=ds, name="Python Data Science", proficiency=85, color_class="bg-primary", order=3)

        # Programming Category
        prog, _ = SkillCategory.objects.get_or_create(
            name="Programming & Tools",
            icon_class="fas fa-laptop-code",
            order=2
        )
        Skill.objects.get_or_create(category=prog, name="Survey Solutions/ODK", proficiency=95, color_class="bg-success", order=1)
        Skill.objects.get_or_create(category=prog, name="Database Management", proficiency=90, color_class="bg-success", order=2)
        Skill.objects.get_or_create(category=prog, name="Web Development", proficiency=85, color_class="bg-success", order=3)

        self.stdout.write(self.style.SUCCESS("Skills seeded successfully!"))
