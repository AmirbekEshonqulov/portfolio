from django.conf import settings

from .i18n import get_dict, SUPPORTED_LANGUAGES


def site_context(request):
    """
    Injects, on every template render:
      - LANG: current language code ('en' | 'ru' | 'uz' | 'de')
      - T: dict of static UI translations for that language
      - SITE_LANGUAGES: list of (code, label) for the language switcher
    """
    lang = getattr(request, "LANG", settings.DEFAULT_LANGUAGE)
    return {
        "LANG": lang,
        "T": get_dict(lang),
        "SITE_LANGUAGES": settings.SITE_LANGUAGES,
    }
