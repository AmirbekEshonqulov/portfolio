"""
Custom Django Admin configuration for the portfolio CMS.

Organised into logical sections matching the live site's sections.
Image previews, search, ordering, and fieldsets make Admin feel like a
real CMS, not just a database editor.
"""

from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.html import format_html

from .models import (
    About, Certificate, Project, Skill,
    SiteSettings, SocialLink, TimelineEntry,
)

# ---------------------------------------------------------------------------
# Admin site branding
# ---------------------------------------------------------------------------
admin.site.site_header = "Amirbek Portfolio CMS"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Content Management Dashboard"


# ---------------------------------------------------------------------------
# SiteSettings (singleton)
# ---------------------------------------------------------------------------
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("🌐 Identity", {
            "fields": ("site_title", "hero_name"),
        }),
        ("📝 Tagline (4 languages)", {
            "fields": ("tagline_en", "tagline_ru", "tagline_uz", "tagline_de"),
            "classes": ("collapse",),
        }),
        ("🦸 Hero Headline", {
            "fields": (
                "hero_headline_en", "hero_headline_ru",
                "hero_headline_uz", "hero_headline_de",
            ),
            "classes": ("collapse",),
        }),
        ("🦸 Hero Bio", {
            "fields": (
                "hero_bio_en", "hero_bio_ru",
                "hero_bio_uz", "hero_bio_de",
            ),
            "classes": ("collapse",),
        }),
        ("📊 Hero Stats", {
            "fields": (
                "stat1_value", "stat1_label_en", "stat1_label_ru", "stat1_label_uz", "stat1_label_de",
                "stat2_value", "stat2_label_en", "stat2_label_ru", "stat2_label_uz", "stat2_label_de",
                "stat3_value", "stat3_label_en", "stat3_label_ru", "stat3_label_uz", "stat3_label_de",
            ),
            "classes": ("collapse",),
        }),
        ("📬 Contact", {
            "fields": ("email", "is_available"),
        }),
        ("👁️ Section Visibility", {
            "fields": (
                "show_about", "show_skills",
                "show_certificates", "show_portfolio", "show_contact",
            ),
        }),
        ("🔍 SEO", {
            "fields": ("seo_title", "seo_description"),
            "classes": ("collapse",),
        }),
        ("🔗 Footer", {
            "fields": ("footer_text_en", "footer_text_ru", "footer_text_uz", "footer_text_de"),
            "classes": ("collapse",),
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# ---------------------------------------------------------------------------
# About (singleton)
# ---------------------------------------------------------------------------
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    fieldsets = (
        ("📄 Bio — Paragraph 1", {
            "fields": ("bio_p1_en", "bio_p1_ru", "bio_p1_uz", "bio_p1_de"),
        }),
        ("📄 Bio — Paragraph 2", {
            "fields": ("bio_p2_en", "bio_p2_ru", "bio_p2_uz", "bio_p2_de"),
        }),
        ("📄 Bio — Paragraph 3", {
            "fields": ("bio_p3_en", "bio_p3_ru", "bio_p3_uz", "bio_p3_de"),
        }),
        ("🏷️ Chips / Tags", {
            "fields": (
                "chip1_en", "chip1_ru", "chip1_uz", "chip1_de",
                "chip2_en", "chip2_ru", "chip2_uz", "chip2_de",
                "chip3_en", "chip3_ru", "chip3_uz", "chip3_de",
                "chip4_en", "chip4_ru", "chip4_uz", "chip4_de",
            ),
        }),
    )

    def has_add_permission(self, request):
        return not About.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# ---------------------------------------------------------------------------
# TimelineEntry
# ---------------------------------------------------------------------------
@admin.register(TimelineEntry)
class TimelineEntryAdmin(admin.ModelAdmin):
    list_display = ("order", "year", "title_en", "is_current")
    list_editable = ("order", "is_current")
    list_display_links = ("title_en",)
    ordering = ("order",)
    fieldsets = (
        ("📅 Year Label", {
            "fields": ("year", "year_ru", "year_uz", "year_de", "is_current", "order"),
        }),
        ("🇬🇧 English", {"fields": ("title_en", "description_en")}),
        ("🇷🇺 Russian", {"fields": ("title_ru", "description_ru"), "classes": ("collapse",)}),
        ("🇺🇿 Uzbek",   {"fields": ("title_uz", "description_uz"), "classes": ("collapse",)}),
        ("🇩🇪 German",  {"fields": ("title_de", "description_de"), "classes": ("collapse",)}),
    )


# ---------------------------------------------------------------------------
# Skill
# ---------------------------------------------------------------------------
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("order", "name_en", "category", "percentage_bar", "is_active", "updated_at")
    list_editable = ("order", "is_active")
    list_display_links = ("name_en",)
    list_filter = ("is_active", "category")
    search_fields = ("name_en", "name_ru", "name_uz", "name_de", "category")
    ordering = ("order", "name_en")

    fieldsets = (
        ("⚙️ Settings", {"fields": ("percentage", "category", "order", "is_active")}),
        ("🎨 Icon", {"fields": ("icon", "icon_svg"), "classes": ("collapse",)}),
        ("🇬🇧 English", {"fields": ("name_en", "description_en")}),
        ("🇷🇺 Russian", {"fields": ("name_ru", "description_ru"), "classes": ("collapse",)}),
        ("🇺🇿 Uzbek",   {"fields": ("name_uz", "description_uz"), "classes": ("collapse",)}),
        ("🇩🇪 German",  {"fields": ("name_de", "description_de"), "classes": ("collapse",)}),
    )

    @admin.display(description="Level")
    def percentage_bar(self, obj):
        pct = obj.percentage
        color = "#00ff88" if pct >= 70 else "#ffb454" if pct >= 40 else "#ff6b6b"
        return format_html(
            '<div style="background:#111;border-radius:4px;width:120px;height:10px;">'
            '<div style="background:{};width:{}%;height:100%;border-radius:4px;"></div>'
            "</div> <span style='font-size:11px;color:#aaa'>{}&thinsp;%</span>",
            color, pct, pct,
        )


# ---------------------------------------------------------------------------
# Certificate
# ---------------------------------------------------------------------------
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("order", "image_preview", "title_en", "issuer", "date_issued", "is_active")
    list_editable = ("order", "is_active")
    list_display_links = ("title_en",)
    list_filter = ("is_active",)
    search_fields = ("title_en", "issuer")
    ordering = ("order",)
    readonly_fields = ("image_preview",)

    fieldsets = (
        ("🎖️ Certificate Info", {
            "fields": ("issuer", "date_issued", "credential_url", "order", "is_active"),
        }),
        ("🖼️ Image", {
            "fields": ("image", "image_preview"),
        }),
        ("🇬🇧 English", {"fields": ("title_en",)}),
        ("🇷🇺 Russian", {"fields": ("title_ru",), "classes": ("collapse",)}),
        ("🇺🇿 Uzbek",   {"fields": ("title_uz",), "classes": ("collapse",)}),
        ("🇩🇪 German",  {"fields": ("title_de",), "classes": ("collapse",)}),
    )


# ---------------------------------------------------------------------------
# Project
# ---------------------------------------------------------------------------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "order", "image_preview", "title_en", "technologies",
        "has_live_url", "has_github", "is_featured", "is_active",
    )
    list_editable = ("order", "is_featured", "is_active")
    list_display_links = ("title_en",)
    list_filter = ("is_active", "is_featured")
    search_fields = ("title_en", "title_ru", "technologies")
    ordering = ("-is_featured", "order")
    readonly_fields = ("image_preview",)

    fieldsets = (
        ("📌 Project Settings", {
            "fields": ("technologies", "live_url", "github_url", "case_study_url",
                       "is_featured", "order", "is_active"),
        }),
        ("🖼️ Cover Image", {
            "fields": ("image", "image_preview"),
        }),
        ("🇬🇧 English", {"fields": ("title_en", "description_en")}),
        ("🇷🇺 Russian", {"fields": ("title_ru", "description_ru"), "classes": ("collapse",)}),
        ("🇺🇿 Uzbek",   {"fields": ("title_uz", "description_uz"), "classes": ("collapse",)}),
        ("🇩🇪 German",  {"fields": ("title_de", "description_de"), "classes": ("collapse",)}),
    )

    @admin.display(description="Live", boolean=True)
    def has_live_url(self, obj):
        return bool(obj.live_url)

    @admin.display(description="GitHub", boolean=True)
    def has_github(self, obj):
        return bool(obj.github_url)


# ---------------------------------------------------------------------------
# SocialLink
# ---------------------------------------------------------------------------
@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("order", "colored_platform", "platform_name", "url_link", "is_active")
    list_editable = ("order", "is_active")
    list_display_links = ("platform_name",)
    ordering = ("order",)

    fieldsets = (
        ("🔗 Link", {
            "fields": ("platform", "platform_name", "url", "order", "is_active"),
        }),
        ("🎨 Custom Icon SVG (optional)", {
            "fields": ("icon_svg",),
            "classes": ("collapse",),
        }),
    )

    @admin.display(description="Platform")
    def colored_platform(self, obj):
        color = obj.color()
        return format_html(
            '<span style="display:inline-block;width:10px;height:10px;'
            'border-radius:50%;background:{};margin-right:6px;"></span>{}',
            color, obj.get_platform_display(),
        )

    @admin.display(description="URL")
    def url_link(self, obj):
        return format_html('<a href="{}" target="_blank" rel="noopener">{}</a>', obj.url, obj.url[:45] + ("…" if len(obj.url) > 45 else ""))
