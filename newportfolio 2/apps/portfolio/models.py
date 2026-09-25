"""
Portfolio app models. All user-visible content is managed from Django Admin.

Multilingual strategy:
  - Each model carries `<field>_en`, `<field>_ru`, `<field>_uz`, `<field>_de`
    columns for the four supported languages.
  - The template tag `{% tr obj "field" %}` (in core/templatetags/i18n_extras.py)
    reads the right column automatically; English is the fallback.
  - This keeps everything in one row and makes Admin editing crystal-clear
    (one fieldset per language), with zero external packages.
"""

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.html import format_html

from apps.core.validators import validate_image_file


# ---------------------------------------------------------------------------
# SiteSettings  (singleton)
# ---------------------------------------------------------------------------
class SiteSettings(models.Model):
    # Identity
    site_title = models.CharField("Site title", max_length=120, default="Amirbek Eshonqulov")
    tagline_en = models.CharField("Tagline (EN)", max_length=120, default="Full-Stack Developer")
    tagline_ru = models.CharField("Tagline (RU)", max_length=120, blank=True)
    tagline_uz = models.CharField("Tagline (UZ)", max_length=120, blank=True)
    tagline_de = models.CharField("Tagline (DE)", max_length=120, blank=True)

    # Hero dynamic content
    hero_name = models.CharField("Developer name shown in hero", max_length=120, default="Amirbek Eshonqulov")

    hero_headline_en = models.CharField("Hero headline (EN)", max_length=200, default="Building the Future of Web with Code")
    hero_headline_ru = models.CharField("Hero headline (RU)", max_length=200, blank=True)
    hero_headline_uz = models.CharField("Hero headline (UZ)", max_length=200, blank=True)
    hero_headline_de = models.CharField("Hero headline (DE)", max_length=200, blank=True)

    hero_bio_en = models.TextField("Hero bio (EN)", blank=True)
    hero_bio_ru = models.TextField("Hero bio (RU)", blank=True)
    hero_bio_uz = models.TextField("Hero bio (UZ)", blank=True)
    hero_bio_de = models.TextField("Hero bio (DE)", blank=True)

    # Stats (hardcoded look, editable values)
    stat1_value = models.CharField("Stat 1 value", max_length=20, default="3+")
    stat1_label_en = models.CharField("Stat 1 label (EN)", max_length=60, default="Years Coding")
    stat1_label_ru = models.CharField("Stat 1 label (RU)", max_length=60, blank=True)
    stat1_label_uz = models.CharField("Stat 1 label (UZ)", max_length=60, blank=True)
    stat1_label_de = models.CharField("Stat 1 label (DE)", max_length=60, blank=True)

    stat2_value = models.CharField("Stat 2 value", max_length=20, default="15+")
    stat2_label_en = models.CharField("Stat 2 label (EN)", max_length=60, default="Projects Delivered")
    stat2_label_ru = models.CharField("Stat 2 label (RU)", max_length=60, blank=True)
    stat2_label_uz = models.CharField("Stat 2 label (UZ)", max_length=60, blank=True)
    stat2_label_de = models.CharField("Stat 2 label (DE)", max_length=60, blank=True)

    stat3_value = models.CharField("Stat 3 value", max_length=20, default="2023")
    stat3_label_en = models.CharField("Stat 3 label (EN)", max_length=60, default="Journey Started")
    stat3_label_ru = models.CharField("Stat 3 label (RU)", max_length=60, blank=True)
    stat3_label_uz = models.CharField("Stat 3 label (UZ)", max_length=60, blank=True)
    stat3_label_de = models.CharField("Stat 3 label (DE)", max_length=60, blank=True)

    # Contact
    email = models.EmailField("Contact email", default="hello@amirbek.dev")
    is_available = models.BooleanField("Available for work?", default=True)

    # Section visibility
    show_about = models.BooleanField("Show About section", default=True)
    show_skills = models.BooleanField("Show Skills section", default=True)
    show_certificates = models.BooleanField("Show Certificates section", default=True)
    show_portfolio = models.BooleanField("Show Portfolio section", default=True)
    show_contact = models.BooleanField("Show Contact section", default=True)

    # SEO
    seo_title = models.CharField("SEO title (override)", max_length=120, blank=True)
    seo_description = models.TextField("SEO meta description", max_length=300, blank=True)

    # Footer
    footer_text_en = models.CharField("Footer text (EN)", max_length=200, blank=True)
    footer_text_ru = models.CharField("Footer text (RU)", max_length=200, blank=True)
    footer_text_uz = models.CharField("Footer text (UZ)", max_length=200, blank=True)
    footer_text_de = models.CharField("Footer text (DE)", max_length=200, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return f"Site Settings (updated {self.updated_at:%Y-%m-%d %H:%M} UTC)"

    def save(self, *args, **kwargs):
        self.pk = 1  # singleton
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


# ---------------------------------------------------------------------------
# About (singleton page section)
# ---------------------------------------------------------------------------
class About(models.Model):
    # Paragraphs
    bio_p1_en = models.TextField("Bio paragraph 1 (EN)", blank=True)
    bio_p1_ru = models.TextField("Bio paragraph 1 (RU)", blank=True)
    bio_p1_uz = models.TextField("Bio paragraph 1 (UZ)", blank=True)
    bio_p1_de = models.TextField("Bio paragraph 1 (DE)", blank=True)

    bio_p2_en = models.TextField("Bio paragraph 2 (EN)", blank=True)
    bio_p2_ru = models.TextField("Bio paragraph 2 (RU)", blank=True)
    bio_p2_uz = models.TextField("Bio paragraph 2 (UZ)", blank=True)
    bio_p2_de = models.TextField("Bio paragraph 2 (DE)", blank=True)

    bio_p3_en = models.TextField("Bio paragraph 3 (EN)", blank=True)
    bio_p3_ru = models.TextField("Bio paragraph 3 (RU)", blank=True)
    bio_p3_uz = models.TextField("Bio paragraph 3 (UZ)", blank=True)
    bio_p3_de = models.TextField("Bio paragraph 3 (DE)", blank=True)

    # Chips / tags under the bio
    chip1_en = models.CharField("Chip 1 (EN)", max_length=80, default="Remote-Ready")
    chip1_ru = models.CharField("Chip 1 (RU)", max_length=80, blank=True)
    chip1_uz = models.CharField("Chip 1 (UZ)", max_length=80, blank=True)
    chip1_de = models.CharField("Chip 1 (DE)", max_length=80, blank=True)

    chip2_en = models.CharField("Chip 2 (EN)", max_length=80, default="Client-Focused")
    chip2_ru = models.CharField("Chip 2 (RU)", max_length=80, blank=True)
    chip2_uz = models.CharField("Chip 2 (UZ)", max_length=80, blank=True)
    chip2_de = models.CharField("Chip 2 (DE)", max_length=80, blank=True)

    chip3_en = models.CharField("Chip 3 (EN)", max_length=80, default="Detail-Obsessed")
    chip3_ru = models.CharField("Chip 3 (RU)", max_length=80, blank=True)
    chip3_uz = models.CharField("Chip 3 (UZ)", max_length=80, blank=True)
    chip3_de = models.CharField("Chip 3 (DE)", max_length=80, blank=True)

    chip4_en = models.CharField("Chip 4 (EN)", max_length=80, default="English & German Friendly")
    chip4_ru = models.CharField("Chip 4 (RU)", max_length=80, blank=True)
    chip4_uz = models.CharField("Chip 4 (UZ)", max_length=80, blank=True)
    chip4_de = models.CharField("Chip 4 (DE)", max_length=80, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def __str__(self):
        return "About Section Content"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


# ---------------------------------------------------------------------------
# TimelineEntry (About timeline items — git-style career log)
# ---------------------------------------------------------------------------
class TimelineEntry(models.Model):
    year = models.CharField("Year / label (e.g. 2023, Today)", max_length=20)
    year_uz = models.CharField("Year label (UZ)", max_length=20, blank=True)
    year_ru = models.CharField("Year label (RU)", max_length=20, blank=True)
    year_de = models.CharField("Year label (DE)", max_length=20, blank=True)

    title_en = models.CharField("Title (EN)", max_length=120)
    title_ru = models.CharField("Title (RU)", max_length=120, blank=True)
    title_uz = models.CharField("Title (UZ)", max_length=120, blank=True)
    title_de = models.CharField("Title (DE)", max_length=120, blank=True)

    description_en = models.CharField("Description (EN)", max_length=300)
    description_ru = models.CharField("Description (RU)", max_length=300, blank=True)
    description_uz = models.CharField("Description (UZ)", max_length=300, blank=True)
    description_de = models.CharField("Description (DE)", max_length=300, blank=True)

    is_current = models.BooleanField("Is current / pulsing dot", default=False)
    order = models.PositiveIntegerField("Order", default=0, db_index=True)

    class Meta:
        verbose_name = "Timeline Entry"
        verbose_name_plural = "Timeline Entries"
        ordering = ["order"]

    def __str__(self):
        return f"{self.year} — {self.title_en}"


# ---------------------------------------------------------------------------
# Skill
# ---------------------------------------------------------------------------
class Skill(models.Model):
    name_en = models.CharField("Name (EN)", max_length=100)
    name_ru = models.CharField("Name (RU)", max_length=100, blank=True)
    name_uz = models.CharField("Name (UZ)", max_length=100, blank=True)
    name_de = models.CharField("Name (DE)", max_length=100, blank=True)

    description_en = models.CharField("Description (EN)", max_length=300, blank=True)
    description_ru = models.CharField("Description (RU)", max_length=300, blank=True)
    description_uz = models.CharField("Description (UZ)", max_length=300, blank=True)
    description_de = models.CharField("Description (DE)", max_length=300, blank=True)

    # Icon: a single emoji or a very short SVG-path string
    icon = models.CharField(
        "Icon (emoji e.g. 🐍 or leave blank for default)",
        max_length=20, blank=True
    )
    icon_svg = models.TextField(
        "SVG icon (optional, replaces emoji — paste a clean <svg> tag)",
        blank=True,
    )

    percentage = models.PositiveIntegerField(
        "Skill level (0–100)",
        default=80,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    category = models.CharField(
        "Category (e.g. Backend, Frontend, DevOps)",
        max_length=80, blank=True
    )
    order = models.PositiveIntegerField("Order", default=0, db_index=True)
    is_active = models.BooleanField("Show on site", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ["order", "name_en"]

    def __str__(self):
        return f"{self.name_en} ({self.percentage}%)"


# ---------------------------------------------------------------------------
# Certificate
# ---------------------------------------------------------------------------
class Certificate(models.Model):
    title_en = models.CharField("Title (EN)", max_length=200)
    title_ru = models.CharField("Title (RU)", max_length=200, blank=True)
    title_uz = models.CharField("Title (UZ)", max_length=200, blank=True)
    title_de = models.CharField("Title (DE)", max_length=200, blank=True)

    issuer = models.CharField("Issuer / organization", max_length=200, blank=True)
    date_issued = models.CharField("Date (e.g. May 2025)", max_length=100, blank=True)
    image = models.ImageField(
        "Certificate image", upload_to="certificates/", blank=True, null=True,
        validators=[validate_image_file],
    )
    credential_url = models.URLField("Credential / verification URL", blank=True)
    order = models.PositiveIntegerField("Order", default=0, db_index=True)
    is_active = models.BooleanField("Show on site", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title_en

    def image_preview(self):
        if self.image:
            return format_html('<img src="{}" style="height:60px;border-radius:4px;" />', self.image.url)
        return "—"
    image_preview.short_description = "Preview"


# ---------------------------------------------------------------------------
# Project
# ---------------------------------------------------------------------------
class Project(models.Model):
    title_en = models.CharField("Title (EN)", max_length=200)
    title_ru = models.CharField("Title (RU)", max_length=200, blank=True)
    title_uz = models.CharField("Title (UZ)", max_length=200, blank=True)
    title_de = models.CharField("Title (DE)", max_length=200, blank=True)

    description_en = models.TextField("Description (EN)", blank=True)
    description_ru = models.TextField("Description (RU)", blank=True)
    description_uz = models.TextField("Description (UZ)", blank=True)
    description_de = models.TextField("Description (DE)", blank=True)

    image = models.ImageField(
        "Project screenshot / cover", upload_to="projects/", blank=True, null=True,
        validators=[validate_image_file],
    )
    # Technologies as a comma-separated string for simplicity
    technologies = models.CharField(
        "Technologies (comma-separated, e.g. Python, Django, JavaScript)",
        max_length=400, blank=True,
    )

    live_url = models.URLField("Live demo URL", blank=True)
    github_url = models.URLField("GitHub repository URL", blank=True)
    case_study_url = models.URLField("Case study / article URL", blank=True)

    is_featured = models.BooleanField("Featured project (shown first)", default=False)
    order = models.PositiveIntegerField("Order", default=0, db_index=True)
    is_active = models.BooleanField("Show on site", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-is_featured", "order", "-created_at"]

    def __str__(self):
        return self.title_en

    def image_preview(self):
        if self.image:
            return format_html('<img src="{}" style="height:60px;border-radius:4px;" />', self.image.url)
        return "—"
    image_preview.short_description = "Preview"

    def tech_list(self):
        """Return list of technology tags from the comma-separated field."""
        return [t.strip() for t in self.technologies.split(",") if t.strip()]


# ---------------------------------------------------------------------------
# SocialLink
# ---------------------------------------------------------------------------
PLATFORM_COLOR_MAP = {
    "github":    "#6e40c9",
    "linkedin":  "#0A66C2",
    "telegram":  "#229ED9",
    "instagram": "#E1306C",
    "facebook":  "#1877F2",
    "twitter":   "#1DA1F2",
    "youtube":   "#FF0000",
    "kwork":     "#5cd25c",
    "email":     "#00ff88",
}


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ("github", "GitHub"),
        ("linkedin", "LinkedIn"),
        ("telegram", "Telegram"),
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("twitter", "Twitter / X"),
        ("youtube", "YouTube"),
        ("kwork", "Kwork"),
        ("email", "Email"),
        ("other", "Other"),
    ]

    platform = models.CharField(
        "Platform", max_length=30, choices=PLATFORM_CHOICES, default="other"
    )
    platform_name = models.CharField(
        "Display name (overrides platform label if set)", max_length=100, blank=True
    )
    url = models.URLField("URL / href")
    icon_svg = models.TextField(
        "Custom SVG icon (optional — leave blank to use built-in icon for known platforms)",
        blank=True,
    )
    order = models.PositiveIntegerField("Order", default=0, db_index=True)
    is_active = models.BooleanField("Show on site", default=True)

    class Meta:
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"
        ordering = ["order", "id"]

    def __str__(self):
        return self.get_display_name()

    def get_display_name(self):
        return self.platform_name or self.get_platform_display()

    def color(self):
        return PLATFORM_COLOR_MAP.get(self.platform, "#00ff88")
