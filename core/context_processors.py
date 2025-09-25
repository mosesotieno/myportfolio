from .models import Profile

def portfolio_context(request):
    profile = Profile.objects.filter(is_active=True).first()
    return {
        'portfolio_profile': profile,
    }