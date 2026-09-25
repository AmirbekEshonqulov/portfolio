from django.http import HttpResponse
from django.shortcuts import redirect

from .i18n import SUPPORTED_LANGUAGES
from .middleware import LANG_COOKIE_NAME, LANG_COOKIE_MAX_AGE


def set_language(request):
    """Sets the language cookie and redirects back to where the visitor came from."""
    lang = request.GET.get("lang") or request.POST.get("lang")
    next_url = request.POST.get("next") or request.GET.get("next") or request.META.get("HTTP_REFERER") or "/"
    response = redirect(next_url)
    if lang in SUPPORTED_LANGUAGES:
        response.set_cookie(LANG_COOKIE_NAME, lang, max_age=LANG_COOKIE_MAX_AGE, samesite="Lax")
    return response


def robots_txt(request):
    lines = ["User-agent: *", "Allow: /", "Disallow: /admin/", "Sitemap: /sitemap.xml"]
    return HttpResponse("\n".join(lines), content_type="text/plain")
