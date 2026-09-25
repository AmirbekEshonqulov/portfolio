from django.utils.deprecation import MiddlewareMixin

from .i18n import SUPPORTED_LANGUAGES, DEFAULT_LANGUAGE

LANG_COOKIE_NAME = "site_lang"
LANG_COOKIE_MAX_AGE = 60 * 60 * 24 * 365  # 1 year


class LanguageMiddleware(MiddlewareMixin):
    """
    Resolves the visitor's language for this request, without requiring
    gettext/.po compilation. Priority: ?lang= query param > cookie >
    browser Accept-Language header > default.

    Sets request.LANG (str) and, if a ?lang= param was used, writes a
    cookie so the choice persists across the whole site.
    """

    def process_request(self, request):
        lang = request.GET.get("lang")
        set_cookie = False
        if lang in SUPPORTED_LANGUAGES:
            set_cookie = True
        else:
            lang = request.COOKIES.get(LANG_COOKIE_NAME)
            if lang not in SUPPORTED_LANGUAGES:
                lang = self._from_accept_header(request) or DEFAULT_LANGUAGE
        request.LANG = lang
        request._set_lang_cookie = set_cookie

    def process_response(self, request, response):
        lang = getattr(request, "LANG", None)
        if lang and getattr(request, "_set_lang_cookie", False):
            response.set_cookie(
                LANG_COOKIE_NAME, lang, max_age=LANG_COOKIE_MAX_AGE, samesite="Lax"
            )
        return response

    @staticmethod
    def _from_accept_header(request):
        header = request.META.get("HTTP_ACCEPT_LANGUAGE", "")
        for part in header.split(","):
            code = part.split(";")[0].strip().split("-")[0].lower()
            if code in SUPPORTED_LANGUAGES:
                return code
        return None
