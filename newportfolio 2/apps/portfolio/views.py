from django.shortcuts import render

from .models import About, Certificate, Project, Skill, SiteSettings, SocialLink, TimelineEntry


def home(request):
    settings = SiteSettings.load()
    about = About.load()
    timeline = TimelineEntry.objects.all()
    skills = Skill.objects.filter(is_active=True)
    certificates = Certificate.objects.filter(is_active=True)
    projects = Project.objects.filter(is_active=True)
    social_links = SocialLink.objects.filter(is_active=True)

    context = {
        "settings": settings,
        "about": about,
        "timeline": timeline,
        "skills": skills,
        "certificates": certificates,
        "projects": projects,
        "social_links": social_links,
    }
    return render(request, "home.html", context)
