from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import HeroSection, FunFact, SocialLink, Service, PopUpService, Portfolio, PortfolioPopUp, \
    PortfolioGallery, Experience, Education, Skill


# Create your views here.

def home_view(request):
    hero = HeroSection.objects.first()
    funfacts = FunFact.objects.all()
    social_link = SocialLink.objects.first()
    services = Service.objects.order_by('number')
    pop_up_service = PopUpService.objects.all().order_by('order')
    portfolio = Portfolio.objects.all()
    portfolio_popup = PortfolioPopUp.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    return render(request, 'base/home.html', {
        'hero': hero,
        'funfacts': funfacts,
        'social_link': social_link,
        'services': services,
        'pop_up_service': pop_up_service,
        'portfolio': portfolio,
        'portfolio_popup': portfolio_popup,
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
    })
