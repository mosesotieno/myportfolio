from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST
from .models import Profile, Project, Experience, Education, Skill, ContactMessage
from .forms import ContactForm

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import Profile, Project, Experience, Education, Skill, ContactMessage, Publication, Referee
from .forms import ContactForm

def home(request):
    profile = Profile.objects.filter(is_active=True).first()
    skills = Skill.objects.filter(show_on_main=True).select_related('category')
    featured_projects = Project.objects.filter(featured=True)[:6]
    experiences = Experience.objects.all()[:3]  # Show latest 3
    publications = Publication.objects.all()[:3]  # Add this line for homepage
    
    context = {
        'profile': profile,
        'skills': skills,
        'featured_projects': featured_projects,
        'experiences': experiences,
        'publications': publications,  # Add this line
    }
    return render(request, 'core/home.html', context)

def about(request):
    profile = Profile.objects.filter(is_active=True).first()
    skills = Skill.objects.all().select_related('category')
    experiences = Experience.objects.all()
    education = Education.objects.all()
    publications = Publication.objects.all()[:3]  # Latest publications
    referees = Referee.objects.all()
    
    # Group skills by category
    skill_categories = {}
    for skill in skills:
        if skill.category not in skill_categories:
            skill_categories[skill.category] = []
        skill_categories[skill.category].append(skill)
    
    context = {
        'profile': profile,
        'skill_categories': skill_categories,
        'experiences': experiences,
        'education': education,
        'publications': publications,
        'referees': referees,
    }
    return render(request, 'core/about.html', context)

# ... rest of your views remain the same ...

class ProjectListView(ListView):
    model = Project
    template_name = 'core/projects.html'
    context_object_name = 'projects'
    paginate_by = 9

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'core/project_detail.html'
    context_object_name = 'project'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

def about(request):
    profile = Profile.objects.filter(is_active=True).first()
    skills = Skill.objects.all().select_related('category')
    experiences = Experience.objects.all()
    education = Education.objects.all()
    
    # Group skills by category
    skill_categories = {}
    for skill in skills:
        if skill.category not in skill_categories:
            skill_categories[skill.category] = []
        skill_categories[skill.category].append(skill)
    
    context = {
        'profile': profile,
        'skill_categories': skill_categories,
        'experiences': experiences,
        'education': education,
    }
    return render(request, 'core/about.html', context)

def contact(request):
    profile = Profile.objects.filter(is_active=True).first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save message to database
            message = ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                ip_address=get_client_ip(request)
            )
            
            # Send email notification - Use profile email as fallback
            contact_email = getattr(settings, 'CONTACT_EMAIL', profile.email if profile else settings.DEFAULT_FROM_EMAIL)
            
            send_mail(
                f"Portfolio Contact: {form.cleaned_data['subject']}",
                f"From: {form.cleaned_data['name']} ({form.cleaned_data['email']})\n\nMessage:\n{form.cleaned_data['message']}\n\nIP: {get_client_ip(request)}",
                settings.DEFAULT_FROM_EMAIL,
                [contact_email],
                fail_silently=False,
            )
            
            return JsonResponse({'success': True, 'message': 'Thank you for your message! I\'ll get back to you soon.'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
    # GET request - show contact form
    context = {
        'profile': profile,
    }
    return render(request, 'core/contact.html', context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip