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
    PUBLICATION_TYPES = [
        ("journal", "Journal Article"),
        ("conference", "Conference Paper"),
        ("report", "Technical Report"),
        ("book", "Book / Chapter"),
        ("other", "Other"),
    ]

    title = models.TextField()
    authors = models.TextField(blank=True, help_text="List of authors as they appear in the publication")
    abstract = models.TextField(blank=True)
    journal = models.CharField(max_length=300, blank=True)
    year = models.PositiveIntegerField()
    publication_type = models.CharField(max_length=50, choices=PUBLICATION_TYPES, default="journal")

    doi = models.CharField(max_length=200, blank=True, help_text="DOI identifier if available")
    link = models.URLField(blank=True, help_text="Direct link to publication online")
    pdf = models.FileField(upload_to="publications/pdfs/", blank=True, null=True)

    topics = TaggableManager(blank=True, help_text="Add keywords or research topics")

    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-year", "order"]

    def __str__(self):
        return f"{self.title} ({self.year})"

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

class Project(models.Model):
    PROJECT_TYPES = [
        ('web', 'Web Application'),
        ('mobile', 'Mobile Application'),
        ('desktop', 'Desktop Application'),
        ('data-science', 'Data Science / Analysis'),
        ('research', 'Research Project'),
        ('other', 'Other'),

    ]

    ICON_CHOICES = [
        ('fas fa-code', 'Code'),
        ('fas fa-database', 'Database'),
        ('fas fa-chart-line', 'Chart / Analytics'),
        ('fas fa-virus', 'Health / Virus'),
        ('fas fa-cloud-sun', 'Climate / Weather'),
        ('fas fa-female', 'Female / Gender'),
        ('fas fa-mobile-alt', 'Mobile'),
        ('fas fa-laptop', 'Laptop'),
        ('fas fa-project-diagram', 'Project'),
    ]

    BG_CHOICES = [
        ('bg-primary', 'Primary'),
        ('bg-success', 'Success'),
        ('bg-warning', 'Warning'),
        ('bg-danger', 'Danger'),
        ('bg-info', 'Info'),
        ('bg-dark', 'Dark'),
        ('bg-light', 'Light'),
    ]

    TEXT_COLOR_CHOICES = [
        ('text-white', 'White'),
        ('text-dark', 'Dark'),
        ('text-muted', 'Muted'),
    ]

    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES, default='web')

    # New fields for styling
    icon_class = models.CharField(max_length=50, choices=ICON_CHOICES, default='fas fa-code')
    background_class = models.CharField(max_length=20, choices=BG_CHOICES, default='bg-light')
    text_color_class = models.CharField(max_length=20, choices=TEXT_COLOR_CHOICES, default='text-white')
    card_class = models.CharField(max_length=50, blank=True, default="")

    # Project details
    featured_image = models.ImageField(upload_to='projects/', blank=True)
    demo_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    button_text = models.CharField(max_length=50, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    # Metadata
    technologies_used = TaggableManager()
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', 'order', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:project_detail', kwargs={'slug': self.slug})

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
    
class Specialization(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=100)  # e.g. "fas fa-virus-slash fa-3x text-primary"

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
    
class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, blank=True, help_text="FontAwesome class, e.g. 'fas fa-chart-bar'")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(help_text="Percentage 0–100")
    color_class = models.CharField(
        max_length=20,
        choices=[
            ("bg-primary", "Primary"),
            ("bg-success", "Success"),
            ("bg-warning", "Warning"),
            ("bg-danger", "Danger"),
            ("bg-info", "Info"),
        ],
        default="bg-primary"
    )
    order = models.PositiveIntegerField(default=0)

    # 👇 new field
    show_on_main = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"