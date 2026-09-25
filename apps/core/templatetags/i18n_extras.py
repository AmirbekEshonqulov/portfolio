from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def tr(context, obj, field):
    """
    Returns the translated value of `field` on `obj` for the current
    request language, e.g. {% tr project "title" %} looks up
    project.title_<LANG>, falling back to the English field, then to
    an empty string.
    """
    if obj is None:
        return ""
    lang = context.get("LANG", "en")
    value = getattr(obj, f"{field}_{lang}", None)
    if value:
        return value
    return getattr(obj, f"{field}_en", "") or ""


@register.filter
def split(value, sep=","):
    if not value:
        return []
    return [v.strip() for v in value.split(sep) if v.strip()]


@register.filter
def modulo(value, arg):
    """{{ forloop.counter|modulo:3 }} -> used to cycle reveal-animation delay classes."""
    try:
        return int(value) % int(arg)
    except (TypeError, ValueError):
        return 0
