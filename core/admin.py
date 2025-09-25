from django.contrib import admin
from .models import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'project_type',
        'category',
        'status',
        'featured',
        'order',
        'start_date',
        'end_date',
    ]
    list_filter = [
        'project_type',
        'category',
        'status',
        'featured',
        'created_at',
    ]
    list_editable = [
        'featured',
        'order',
        'status',
    ]
    search_fields = [
        'title',
        'description',
        'short_description',
        'category',
    ]
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-featured', 'order', '-created_at']
    fieldsets = (
        ("Basic Info", {
            "fields": ("title", "slug", "description", "short_description", "project_type")
        }),
        ("Visuals & Styling", {
            "fields": ("icon_class", "background_class", "text_color_class", "card_class", "featured_image")
        }),
        ("Project Details", {
            "fields": ("demo_url", "github_url", "button_text", "start_date", "end_date")
        }),
        ("Metadata", {
            "fields": ("technologies_used", "category", "status", "featured", "order")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )
    readonly_fields = ("created_at", "updated_at")

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'current']
    list_filter = ['experience_type', 'current']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    list_filter = ['read', 'created_at']
    readonly_fields = ['created_at', 'ip_address']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "year",
        "publication_type",
        "journal",
        "featured",
        "order",
    )
    list_filter = ("year", "publication_type", "featured")
    search_fields = ("title", "authors", "journal", "doi")
    ordering = ("-year", "order")
    list_editable = ("featured", "order")
    prepopulated_fields = {}  # not needed unless you add slug

    fieldsets = (
        (None, {
            "fields": ("title", "authors", "abstract", "journal", "year", "publication_type")
        }),
        ("Links", {
            "fields": ("doi", "link", "pdf")
        }),
        ("Metadata", {
            "fields": ("topics", "featured", "order")
        }),
    )


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "order"]
    ordering = ["order"]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "proficiency", "order"]
    list_filter = ["category"]
    ordering = ["category", "order"]

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "icon_class"]
    list_filter = ["title"]
    ordering = ["title", "order"]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "email"]
    list_filter = ["name"]
    ordering = ["name"]