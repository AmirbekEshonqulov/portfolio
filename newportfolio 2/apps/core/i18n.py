"""
Lightweight, dependency-free translation dictionary for static UI copy
(navigation, section labels, buttons, empty/error states).

Why not Django's gettext/.po files? gettext requires the `msgfmt` binary to
compile .po -> .mo on every environment this project is deployed to. A plain
Python dictionary needs no compilation step, ships correctly everywhere, and
is trivial to extend. Personal, editorial content (About text, skill
descriptions, project descriptions, certificates...) lives in the database
instead (see apps/portfolio/models.py) so it can be managed from Django
Admin, as required.

Usage in templates: `{{ T.nav_home }}` (T is injected by
apps.core.context_processors.site_context). Usage in Python:
`apps.core.i18n.translate(lang, "nav_home")`.
"""

SUPPORTED_LANGUAGES = ["en", "ru", "uz", "de"]
DEFAULT_LANGUAGE = "en"

TRANSLATIONS = {
    "en": {
        "nav_tag": "DEV.PORTFOLIO",
        "nav_home": "Home", "nav_about": "About", "nav_skills": "Skills",
        "nav_certificates": "Certificates", "nav_portfolio": "Portfolio", "nav_contact": "Contact",
        "hero_cta1": "View Works", "hero_cta2": "Hire Me",
        "about_eyebrow": "// ABOUT ME", "about_title": "The Developer Behind the Code",
        "about_timeline_title": "// TIMELINE.LOG",
        "skills_eyebrow": "// TECH STACK", "skills_title": "Tools I Build With",
        "skills_subtitle": "A focused stack chosen for speed, reliability, and clean architecture.",
        "certificates_eyebrow": "// CREDENTIALS", "certificates_title": "Certificates & Learning",
        "certificates_subtitle": "Courses and credentials that back up the skills above.",
        "certificates_empty": "Certificates will appear here soon.",
        "certificates_view_credential": "View credential",
        "portfolio_eyebrow": "// SELECTED WORK", "portfolio_title": "Projects & Builds",
        "portfolio_subtitle": "A snapshot of products I've designed, coded, and shipped.",
        "portfolio_more_title": "More in Progress",
        "portfolio_more_desc": "New projects are being built right now — let's add yours to the list.",
        "portfolio_start_project": "Start a Project",
        "portfolio_live_demo": "Live Demo", "portfolio_source_code": "GitHub", "portfolio_case_study": "Case Study",
        "portfolio_empty": "Projects are being uploaded — check back soon.",
        "contact_eyebrow": "// GET IN TOUCH", "contact_title": "Let's Build Something Great",
        "contact_subtitle": "Whether you have a project in mind or just want to connect, I'm one message away.",
        "contact_email_label": "Or write directly:",
        "footer_built_with": "Built with code & curiosity.",
        "terminal_whoami": "whoami", "terminal_role": "role", "terminal_stack": "stack",
        "terminal_status": "status", "terminal_deploy": "deploy --target=global_clients",
        "terminal_connection": "connection established: Uzbekistan → Europe",
        "terminal_ready": "ready for collaboration",
        "theme_dark": "Dark", "theme_light": "Light", "theme_toggle_label": "Toggle theme",
        "lang_select_label": "Select language",
        "availability_available": "Available for freelance work",
        "availability_unavailable": "Currently booked",
        "error_404_title": "Page not found", "error_404_desc": "This route doesn't exist — but the rest of the site does.",
        "error_404_back": "Back to home",
        "skip_to_content": "Skip to content",
        "system_status": "system online",
    },
    "ru": {
        "nav_tag": "DEV.ПОРТФОЛИО",
        "nav_home": "Главная", "nav_about": "Обо мне", "nav_skills": "Навыки",
        "nav_certificates": "Сертификаты", "nav_portfolio": "Портфолио", "nav_contact": "Контакты",
        "hero_cta1": "Смотреть работы", "hero_cta2": "Нанять меня",
        "about_eyebrow": "// ОБО МНЕ", "about_title": "Разработчик за этим кодом",
        "about_timeline_title": "// TIMELINE.LOG",
        "skills_eyebrow": "// ТЕХНОЛОГИИ", "skills_title": "Инструменты, с которыми я работаю",
        "skills_subtitle": "Сфокусированный стек, выбранный за скорость, надёжность и чистую архитектуру.",
        "certificates_eyebrow": "// СЕРТИФИКАТЫ", "certificates_title": "Сертификаты и обучение",
        "certificates_subtitle": "Курсы и сертификаты, подтверждающие навыки выше.",
        "certificates_empty": "Сертификаты скоро появятся здесь.",
        "certificates_view_credential": "Смотреть сертификат",
        "portfolio_eyebrow": "// ИЗБРАННЫЕ РАБОТЫ", "portfolio_title": "Проекты и разработки",
        "portfolio_subtitle": "Краткий обзор продуктов, которые я спроектировал, написал и запустил.",
        "portfolio_more_title": "В разработке",
        "portfolio_more_desc": "Прямо сейчас создаются новые проекты — добавим в список и ваш.",
        "portfolio_start_project": "Начать проект",
        "portfolio_live_demo": "Демо", "portfolio_source_code": "GitHub", "portfolio_case_study": "Кейс",
        "portfolio_empty": "Проекты добавляются — загляните позже.",
        "contact_eyebrow": "// СВЯЗАТЬСЯ", "contact_title": "Создадим что-то великое",
        "contact_subtitle": "Если у вас есть идея проекта или вы просто хотите познакомиться — я на расстоянии одного сообщения.",
        "contact_email_label": "Или напишите напрямую:",
        "footer_built_with": "Создано с кодом и любопытством.",
        "terminal_whoami": "whoami", "terminal_role": "role", "terminal_stack": "stack",
        "terminal_status": "status", "terminal_deploy": "deploy --target=global_clients",
        "terminal_connection": "соединение установлено: Узбекистан → Европа",
        "terminal_ready": "готов к сотрудничеству",
        "theme_dark": "Тёмная", "theme_light": "Светлая", "theme_toggle_label": "Переключить тему",
        "lang_select_label": "Выбор языка",
        "availability_available": "Доступен для фриланс-проектов",
        "availability_unavailable": "Сейчас занят",
        "error_404_title": "Страница не найдена", "error_404_desc": "Такого маршрута нет — но остальной сайт на месте.",
        "error_404_back": "На главную",
        "skip_to_content": "Перейти к содержимому",
        "system_status": "система в сети",
    },
    "uz": {
        "nav_tag": "DEV.PORTFOLIO",
        "nav_home": "Bosh sahifa", "nav_about": "Men haqimda", "nav_skills": "Ko'nikmalar",
        "nav_certificates": "Sertifikatlar", "nav_portfolio": "Portfolio", "nav_contact": "Aloqa",
        "hero_cta1": "Ishlarni ko'rish", "hero_cta2": "Meni yollang",
        "about_eyebrow": "// MEN HAQIMDA", "about_title": "Kod ortidagi dasturchi",
        "about_timeline_title": "// TIMELINE.LOG",
        "skills_eyebrow": "// TEXNOLOGIYALAR", "skills_title": "Men ishlatadigan vositalar",
        "skills_subtitle": "Tezlik, ishonchlilik va toza arxitektura uchun tanlangan fokuslangan stack.",
        "certificates_eyebrow": "// SERTIFIKATLAR", "certificates_title": "Sertifikatlar va o'quv",
        "certificates_subtitle": "Yuqoridagi ko'nikmalarni tasdiqlovchi kurslar va sertifikatlar.",
        "certificates_empty": "Sertifikatlar tez orada shu yerda chiqadi.",
        "certificates_view_credential": "Sertifikatni ko'rish",
        "portfolio_eyebrow": "// TANLANGAN ISHLAR", "portfolio_title": "Loyihalar va ishlanmalar",
        "portfolio_subtitle": "Men loyihalashtirib, yozib, ishga tushirgan mahsulotlardan namuna.",
        "portfolio_more_title": "Hozir ishlanmoqda",
        "portfolio_more_desc": "Hozir yangi loyihalar ustida ishlanmoqda — sizning loyihangizni ham ro'yxatga qo'shamiz.",
        "portfolio_start_project": "Loyihani boshlash",
        "portfolio_live_demo": "Demo", "portfolio_source_code": "GitHub", "portfolio_case_study": "Case Study",
        "portfolio_empty": "Loyihalar yuklanmoqda — birozdan so'ng qayta tashrif buyuring.",
        "contact_eyebrow": "// ALOQAGA CHIQISH", "contact_title": "Birgalikda ajoyib narsa yarataylik",
        "contact_subtitle": "Loyihangiz bo'lsa ham, shunchaki tanishmoqchi bo'lsangiz ham — men bir xabar narida.",
        "contact_email_label": "Yoki to'g'ridan-to'g'ri yozing:",
        "footer_built_with": "Kod va qiziqish bilan yaratilgan.",
        "terminal_whoami": "whoami", "terminal_role": "role", "terminal_stack": "stack",
        "terminal_status": "status", "terminal_deploy": "deploy --target=global_clients",
        "terminal_connection": "aloqa o'rnatildi: O'zbekiston → Yevropa",
        "terminal_ready": "hamkorlikka tayyor",
        "theme_dark": "Tungi", "theme_light": "Kunduzgi", "theme_toggle_label": "Mavzuni almashtirish",
        "lang_select_label": "Tilni tanlash",
        "availability_available": "Freelance loyihalarga tayyorman",
        "availability_unavailable": "Hozircha band",
        "error_404_title": "Sahifa topilmadi", "error_404_desc": "Bu manzil mavjud emas — lekin sayt qolgan qismi ishlayapti.",
        "error_404_back": "Bosh sahifaga",
        "skip_to_content": "Kontentga o'tish",
        "system_status": "tizim onlayn",
    },
    "de": {
        "nav_tag": "DEV.PORTFOLIO",
        "nav_home": "Start", "nav_about": "Über mich", "nav_skills": "Fähigkeiten",
        "nav_certificates": "Zertifikate", "nav_portfolio": "Portfolio", "nav_contact": "Kontakt",
        "hero_cta1": "Projekte ansehen", "hero_cta2": "Mich engagieren",
        "about_eyebrow": "// ÜBER MICH", "about_title": "Der Entwickler hinter dem Code",
        "about_timeline_title": "// TIMELINE.LOG",
        "skills_eyebrow": "// TECH-STACK", "skills_title": "Werkzeuge, mit denen ich arbeite",
        "skills_subtitle": "Ein fokussierter Stack, gewählt für Geschwindigkeit, Zuverlässigkeit und saubere Architektur.",
        "certificates_eyebrow": "// ZERTIFIKATE", "certificates_title": "Zertifikate & Weiterbildung",
        "certificates_subtitle": "Kurse und Zertifikate, die die obigen Fähigkeiten belegen.",
        "certificates_empty": "Zertifikate erscheinen hier in Kürze.",
        "certificates_view_credential": "Zertifikat ansehen",
        "portfolio_eyebrow": "// AUSGEWÄHLTE ARBEITEN", "portfolio_title": "Projekte & Builds",
        "portfolio_subtitle": "Ein Einblick in Produkte, die ich entworfen, programmiert und veröffentlicht habe.",
        "portfolio_more_title": "Weitere in Arbeit",
        "portfolio_more_desc": "Gerade entstehen neue Projekte — lassen Sie uns auch Ihres auf die Liste setzen.",
        "portfolio_start_project": "Projekt starten",
        "portfolio_live_demo": "Live-Demo", "portfolio_source_code": "GitHub", "portfolio_case_study": "Case Study",
        "portfolio_empty": "Projekte werden hochgeladen — schau bald wieder vorbei.",
        "contact_eyebrow": "// KONTAKT AUFNEHMEN", "contact_title": "Lass uns etwas Großes bauen",
        "contact_subtitle": "Egal ob Sie ein konkretes Projekt im Kopf haben oder einfach nur Kontakt aufnehmen möchten — ich bin nur eine Nachricht entfernt.",
        "contact_email_label": "Oder direkt schreiben:",
        "footer_built_with": "Erstellt mit Code & Neugier.",
        "terminal_whoami": "whoami", "terminal_role": "role", "terminal_stack": "stack",
        "terminal_status": "status", "terminal_deploy": "deploy --target=global_clients",
        "terminal_connection": "Verbindung hergestellt: Usbekistan → Europa",
        "terminal_ready": "bereit für Zusammenarbeit",
        "theme_dark": "Dunkel", "theme_light": "Hell", "theme_toggle_label": "Design wechseln",
        "lang_select_label": "Sprache wählen",
        "availability_available": "Verfügbar für Freelance-Projekte",
        "availability_unavailable": "Derzeit ausgebucht",
        "error_404_title": "Seite nicht gefunden", "error_404_desc": "Diese Route gibt es nicht — der Rest der Seite schon.",
        "error_404_back": "Zur Startseite",
        "skip_to_content": "Zum Inhalt springen",
        "system_status": "System online",
    },
}


def translate(lang: str, key: str) -> str:
    lang = lang if lang in SUPPORTED_LANGUAGES else DEFAULT_LANGUAGE
    return TRANSLATIONS.get(lang, {}).get(key, TRANSLATIONS[DEFAULT_LANGUAGE].get(key, key))


def get_dict(lang: str) -> dict:
    lang = lang if lang in SUPPORTED_LANGUAGES else DEFAULT_LANGUAGE
    return TRANSLATIONS.get(lang, TRANSLATIONS[DEFAULT_LANGUAGE])
