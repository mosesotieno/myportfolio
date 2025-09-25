from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils import timezone

class Profile(models.Model):
    # Personal Information
    name = models.CharField(max_length=100, default="Otieno Moses Ochieng")
    title = models.CharField(max_length=200, default="Data Scientist & Statistician")
    email = models.EmailField(default="mosotieno25@gmail.com")
    phone = models.CharField(max_length=20, default="+254-719648375")
    location = models.CharField(max_length=100, default="Kenya")
    bio = models.TextField(default="Expert statistician and data scientist with extensive experience in healthcare research, data management, and programming.")
    short_bio = models.CharField(max_length=300, default="Data Scientist | Statistician | Python & R Expert | Healthcare Research")
    
    # Professional Summary
    career_objective = models.TextField(
        default="To leverage my expertise in statistics, programming and information technology to provide innovative, data-driven solutions and effectively address complex statistical and IT challenges."
    )
    
    # Social Links
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    
    # Images
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True)
    
    # Stats
    years_experience = models.PositiveIntegerField(default=9)  # 2016-2025
    projects_completed = models.PositiveIntegerField(default=15)
    happy_clients = models.PositiveIntegerField(default=8)
    
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Portfolio Profile"
        verbose_name_plural = "Portfolio Profiles"

    def __str__(self):
        return self.name

# Add new models for enhanced CV features
class Publication(models.Model):
    title = models.TextField()
    authors = models.TextField(blank=True)
    journal = models.CharField(max_length=300, blank=True)
    year = models.PositiveIntegerField()
    link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-year', 'order']

    def __str__(self):
        return self.title

class Referee(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.organization}"

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Skill Categories"
        ordering = ['order']

    def __str__(self):
        return self.name

class Skill(models.Model):
    PROFICIENCY_LEVELS = [
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert'),
    ]

    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    proficiency = models.IntegerField(choices=PROFICIENCY_LEVELS, default=3)
    order = models.PositiveIntegerField(default=0)
    show_on_main = models.BooleanField(default=True)

    class Meta:
        ordering = ['category__order', 'order']

    def __str__(self):
        return self.name

    def get_proficiency_percentage(self):
        return (self.proficiency / 4) * 100

class Project(models.Model):
    PROJECT_TYPES = [
        ('web', 'Web Application'),
        ('mobile', 'Mobile Application'),
        ('desktop', 'Desktop Application'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES, default='web')
    
    # Project details
    featured_image = models.ImageField(upload_to='projects/')
    demo_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    # Metadata
    technologies_used = TaggableManager()
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', 'order', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    @property
    def is_ongoing(self):
        return self.end_date is None

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

class Experience(models.Model):
    EXPERIENCE_TYPES = [
        ('job', 'Job'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
        ('education', 'Education'),
    ]

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    experience_type = models.CharField(max_length=20, choices=EXPERIENCE_TYPES, default='job')
    
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    
    description = models.TextField(blank=True)
    responsibilities = models.TextField(blank=True)
    
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-start_date', 'order']

    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    field_of_study = models.CharField(max_length=200, blank=True)
    
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    
    description = models.TextField(blank=True)
    grade = models.CharField(max_length=50, blank=True)
    
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-start_date', 'order']

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name}: {self.subject}"