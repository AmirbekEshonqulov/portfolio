# Amirbek Eshonqulov — Developer Portfolio (Django)

A fully Django-based rebuild of the original static `index.html` portfolio.
Every visible section is now backed by the database and editable from Django
Admin — no more editing HTML to add a skill, certificate, or project.

---

## 1. What the original project was

- `index.html` (1156 lines) — a **single self-contained file**: Tailwind via
  CDN, all CSS in a `<style>` block, all JS (i18n dictionary, terminal
  typing effect, canvas particle background, nav/menu logic) in a `<script>`
  block at the bottom. All content (hero, about, skills, 5 projects) was
  **hardcoded**, duplicated 4× for EN/RU/UZ/DE inside a JS object.
- `script.js` / `style.css` — extracted copies of the above, **not actually
  referenced by `index.html`**, containing unfinished work: an `apiGet()`
  helper that tried to `fetch()` a separate Django REST API for
  Certificates/Skills/Projects/SocialLinks/SiteSettings and append them to
  the static page.
- `admin-backend/` — a separate Django project (`portfolio_admin`) with a
  `content` app exposing that REST API. `DEBUG=True` and a checked-in
  `SECRET_KEY` were hardcoded in `settings.py`; `CORS_ALLOW_ALL_ORIGINS =
  True`. It only modeled the *extra* items appended on top of the hardcoded
  HTML (e.g. `Skill.percent` for bonus skill cards) — the original 6
  skills/5 projects/hero/about copy were not editable at all.

**Problems identified:** duplicated/never-loaded frontend logic; no real
CMS coverage of the primary content; insecure default settings; frontend
and backend were two disconnected codebases (the API layer was built but
never wired up); no certificates section actually rendered on the page;
no image validation on uploads; translations hardcoded 4× in JS.

**What was preserved:** the visual identity (dark, developer/terminal
aesthetic, green accent, glass cards, particle background), the exact
copy in all 4 languages (carried over verbatim into the database seed —
nothing was invented), the real social links, and the Django-admin-as-CMS
direction the original author was already heading in.

---

## 2. New architecture

```
config/                  # Django project (settings, urls, wsgi/asgi)
apps/
  core/                   # cross-cutting: language handling, validators
    i18n.py               # static UI-copy dictionary (4 languages)
    middleware.py          # resolves request.LANG (?lang=, cookie, browser)
    context_processors.py  # injects LANG / T / SITE_LANGUAGES into templates
    validators.py           # upload validation (type + size)
    templatetags/i18n_extras.py   # {% tr obj "field" %}, split, modulo
  portfolio/              # the CMS
    models.py             # SiteSettings, About, TimelineEntry, Skill,
                           # Certificate, Project, SocialLink
    admin.py               # grouped fieldsets, image previews, list-editable
    views.py / urls.py     # single `home` view, all content from the DB
templates/
  base.html                # shell: nav, theme, language, footer, cert modal
  home.html                 # hero → about → skills → certificates →
                             # portfolio → contact
  components/social_icon.html
static/css/main.css        # design tokens, dark+light themes, responsive
static/js/main.js           # theme/lang/menu/reveal/terminal/canvas bg — vanilla JS, no deps
media/                      # uploaded certificate & project images
```

### Why gettext wasn't used for the static UI copy
Django's `{% trans %}` requires compiling `.po → .mo` files with the
`msgfmt` binary on every machine this runs on. That's an easy step to
forget and a common source of "translations don't show up in production"
bugs. Instead, `apps/core/i18n.py` is a plain Python dictionary — zero
compilation, zero extra dependency, works identically everywhere. Personal/
editorial content (bios, skill descriptions, project descriptions,
certificates...) lives in the **database** instead, exactly as required,
with one field per language (`title_en`, `title_ru`, `title_uz`,
`title_de`) rather than 4 duplicated models. The `{% tr obj "field" %}`
template tag reads the right one automatically and falls back to English.

### Language switching
`apps/core/middleware.py` resolves the visitor's language on every request
in this order: `?lang=xx` query param → `site_lang` cookie → browser
`Accept-Language` → English. Clicking a language in the nav sets `?lang=`,
which the middleware turns into a cookie, so the whole site (not just one
page) remembers the choice.

### Theme switching
Dark is the default. A tiny inline script in `<head>` (before any CSS
loads) reads `localStorage.theme` (or `prefers-color-scheme`) and sets
`data-theme` on `<html>` before first paint, so there's no flash of the
wrong theme. `static/js/main.js` handles the toggle button and persists
the choice.

### Background animation
`static/js/main.js` §10 draws, on a single `<canvas>`: slowly drifting,
rotating developer symbols (`{ }`, `< />`, `#`, `$`, `=>`, `01`...) at very
low opacity, plus a light particle network with connecting lines that
subtly reacts to the cursor. Both systems respect
`prefers-reduced-motion`, are capped by screen area (GPU/CPU-friendly),
sit behind everything with `pointer-events: none`, and re-theme their
color automatically when you switch dark/light.

### Security
- `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS` all come
  from environment variables (see `.env.example`), not hardcoded.
- `DEBUG` defaults to `True` only for local convenience — **set
  `DJANGO_DEBUG=False` in production** (this flips on `SECURE_*`/`X_FRAME_OPTIONS`
  settings automatically).
- Certificate/project image uploads are validated for both file extension
  and size (`apps/core/validators.py`, 5MB / .jpg .jpeg .png .webp .gif) —
  tested against a rejected `.exe` and an oversized file.
- No REST API / CORS surface at all anymore — everything is server-rendered
  Django templates, which removes the entire class of issues the old
  `CORS_ALLOW_ALL_ORIGINS = True` API had.
- `/admin/` is disallowed in `robots.txt`.

### Performance
- No frontend framework/build step; one CSS file, one JS file, both plain
  and dependency-free.
- Images are `loading="lazy"`.
- DB queries in `views.home()` are 4 simple filtered querysets — no N+1
  patterns, nothing to paginate yet at this content scale (the schema
  supports scaling to hundreds of skills/projects/certificates without any
  template changes; add `Paginator` in `views.py` later if the project list
  grows very large).

---

## 3. Running it

```bash
cd newportfolio
python -m venv venv && source venv/bin/activate     # optional but recommended
pip install -r requirements.txt

cp .env.example .env        # then edit DJANGO_SECRET_KEY etc.

python manage.py migrate            # creates the DB *and* seeds real content
python manage.py createsuperuser    # your admin login
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the site and `http://127.0.0.1:8000/admin/`
for the CMS. The migration already seeds: site settings, about text,
4-entry timeline, 6 core skills (Python/Django/JavaScript/HTML5/CSS3/
Tailwind), and the real social links (Facebook/Instagram/Telegram/Kwork) —
all in all 4 languages, using the exact original copy, nothing invented.

## 4. Editing content (no code changes, ever)

| To change...                                   | Go to (Admin)                       |
|-------------------------------------------------|--------------------------------------|
| Hero name/headline/bio, stats, email, section visibility, SEO, footer | **Site Settings** |
| About paragraphs & the 4 chips                  | **About Section**                    |
| The Git-style timeline entries                  | **Timeline Entries**                 |
| Skills (add/remove/reorder/% bar)                | **Skills** — `percentage` field, 0–100, drives the bar width live |
| Certificates (unlimited, with image upload)      | **Certificates**                     |
| Projects (unlimited, image + links + tags)       | **Projects**                         |
| Social/contact links (unlimited)                 | **Social Links**                     |

All of the above were verified end-to-end during build: added a Skill at
73%, a Certificate with an uploaded image, and a featured Project with an
uploaded image — all three appeared correctly on the live homepage with
zero source changes, matching the required admin-CRUD test.

## 5. Deploying

1. Set real env vars (`DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`,
   `DJANGO_ALLOWED_HOSTS`, `DJANGO_CSRF_TRUSTED_ORIGINS`).
2. `python manage.py collectstatic` and serve `staticfiles/` + `media/`
   from your web server (nginx/Caddy) or a storage backend.
3. Run with a real WSGI/ASGI server (gunicorn/uvicorn), not
   `runserver`.
4. Put SQLite behind regular backups, or switch `DATABASES` to Postgres —
   the schema has no SQLite-specific features.

## 6. Known limitations / next steps

- SQLite is fine for a single-developer portfolio; move to Postgres if you
  expect concurrent writers.
- No contact form (the Contact section is intentionally just social links
  + a `mailto:` — add a `django.core.mail` form later if you want inbound
  messages instead of outbound-only contact).
- No automated test suite yet (the project was verified via Django's
  system checks + a scripted admin-CRUD smoke test during build, see
  above) — consider adding `apps/portfolio/tests.py` for CI.
- `sitemap.xml` is not wired up yet (`robots.txt` is); add
  `django.contrib.sitemaps` if you want one.
