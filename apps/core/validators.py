import os

from django.conf import settings
from django.core.exceptions import ValidationError


def validate_image_file(file_obj):
    """Reject uploads that are too large or have a disallowed extension.

    Applied to every admin-managed ImageField (certificates, projects) so
    the CMS can't be used to upload arbitrarily large or unsafe files.
    """
    ext = os.path.splitext(file_obj.name)[1].lower()
    allowed = getattr(settings, "ALLOWED_IMAGE_EXTENSIONS", [".jpg", ".jpeg", ".png", ".webp", ".gif"])
    if ext not in allowed:
        raise ValidationError(f"Unsupported file type '{ext}'. Allowed: {', '.join(allowed)}")

    max_mb = getattr(settings, "MAX_UPLOAD_IMAGE_MB", 5)
    if file_obj.size > max_mb * 1024 * 1024:
        raise ValidationError(f"Image is too large. Maximum size is {max_mb}MB.")
