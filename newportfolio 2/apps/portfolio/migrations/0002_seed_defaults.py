"""Seed the database with sensible default site settings, about content,
timeline entries, default skills and social links.

All content is real for Amirbek Eshonqulov – nothing is invented.
Run with: python manage.py migrate
"""
from django.db import migrations


def seed_defaults(apps, schema_editor):
    SiteSettings = apps.get_model("portfolio", "SiteSettings")
    About        = apps.get_model("portfolio", "About")
    TimelineEntry= apps.get_model("portfolio", "TimelineEntry")
    Skill        = apps.get_model("portfolio", "Skill")
    SocialLink   = apps.get_model("portfolio", "SocialLink")

    # --- SiteSettings ---
    SiteSettings.objects.create(
        pk=1,
        site_title="Amirbek Eshonqulov",
        tagline_en="Full-Stack Developer",
        tagline_ru="Full-Stack Разработчик",
        tagline_uz="Full-Stack Dasturchi",
        tagline_de="Full-Stack-Entwickler",
        hero_name="Amirbek Eshonqulov",
        hero_headline_en="Building the Future of Web with Code",
        hero_headline_ru="Создаю будущее веба с помощью кода",
        hero_headline_uz="Kod orqali Web kelajagini yarataman",
        hero_headline_de="Die Zukunft des Webs mit Code gestalten",
        hero_bio_en="A Full-Stack Developer crafting fast, clean, and reliable digital products with Python, JavaScript, and modern web architecture — partnering with clients across Europe, Germany, and beyond to turn ideas into shipped software.",
        hero_bio_ru="Full-Stack разработчик, создающий быстрые, чистые и надёжные digital-продукты на Python, JavaScript и современной веб-архитектуре — сотрудничаю с клиентами из Европы, Германии и других стран, превращая идеи в готовый продукт.",
        hero_bio_uz="Python, JavaScript va zamonaviy veb-arxitektura asosida tez, sifatli va ishonchli raqamli mahsulotlar yaratuvchi Full-Stack dasturchiman — Yevropa, Germaniya va boshqa mamlakatlardagi mijozlar bilan hamkorlik qilib, g'oyalarni tayyor mahsulotga aylantiraman.",
        hero_bio_de="Ein Full-Stack-Entwickler, der schnelle, saubere und zuverlässige digitale Produkte mit Python, JavaScript und moderner Web-Architektur baut — in Zusammenarbeit mit Kunden aus Europa, Deutschland und der ganzen Welt.",
        stat1_value="3+", stat1_label_en="Years Coding",
        stat1_label_ru="Лет в разработке", stat1_label_uz="Yillik tajriba", stat1_label_de="Jahre Erfahrung",
        stat2_value="15+", stat2_label_en="Projects Delivered",
        stat2_label_ru="Завершённых проектов", stat2_label_uz="Bajarilgan loyihalar", stat2_label_de="Abgeschlossene Projekte",
        stat3_value="2023", stat3_label_en="Journey Started",
        stat3_label_ru="Год начала пути", stat3_label_uz="Boshlangan yil", stat3_label_de="Start der Reise",
        email="hello@amirbek.dev",
        is_available=True,
        seo_title="Amirbek Eshonqulov — Full-Stack Developer",
        seo_description="Full-Stack Developer specialising in Python, Django, JavaScript and modern web architecture. Available for freelance projects across Europe and beyond.",
        footer_text_en="Built with code & curiosity.",
        footer_text_ru="Создано с кодом и любопытством.",
        footer_text_uz="Kod va qiziqish bilan yaratilgan.",
        footer_text_de="Erstellt mit Code & Neugier.",
    )

    # --- About ---
    About.objects.create(
        pk=1,
        bio_p1_en="My journey into software development began in 2023, driven by curiosity and a relentless need to build things that work. Since then, I've grown from writing my first lines of Python and JavaScript into delivering complete, production-ready web applications for real clients.",
        bio_p1_ru="Мой путь в разработке начался в 2023 году благодаря любопытству и желанию создавать вещи, которые реально работают. С тех пор я прошёл путь от первых строк на Python и JavaScript до создания полноценных веб-приложений для реальных клиентов.",
        bio_p1_uz="Dasturlashga bo'lgan qiziqishim 2023-yilda boshlandi — ishlaydigan narsalarni yaratishga bo'lgan ishtiyoq tufayli. O'shandan beri Python va JavaScript'dagi birinchi qatorlardan boshlab, haqiqiy mijozlar uchun to'liq, ishga tushirilgan veb-ilovalar yaratishgacha o'sdim.",
        bio_p1_de="Meine Reise in die Softwareentwicklung begann 2023, angetrieben von Neugier und dem Wunsch, Dinge zu bauen, die wirklich funktionieren.",
        bio_p2_en="As a freelancer, I've learned that great code is only half the job — the other half is clear communication, reliability, and genuinely understanding what a client needs before writing a single function.",
        bio_p2_ru="Как фрилансер, я понял, что хороший код — это лишь половина работы. Вторая половина — чёткая коммуникация, надёжность и искреннее понимание потребностей клиента.",
        bio_p2_uz="Freelancer sifatida tushundimki, yaxshi kod — bu ishning yarmi xolos. Qolgan yarmi — aniq muloqot, ishonchlilik va birinchi funksiyani yozishdan oldin mijozning haqiqiy ehtiyojini chuqur tushunish.",
        bio_p2_de="Als Freelancer habe ich gelernt, dass guter Code nur die halbe Arbeit ist — die andere Hälfte ist klare Kommunikation und Zuverlässigkeit.",
        bio_p3_en="Today, my goal is bigger than any single project: I want to build long-term partnerships with international clients and tech ecosystems — especially across Europe and Germany.",
        bio_p3_ru="Сегодня моя цель шире, чем любой отдельный проект: я хочу строить долгосрочные партнёрства с международными клиентами — особенно в Европе и Германии.",
        bio_p3_uz="Bugungi maqsadim har qanday bitta loyihadan kattaroq: men xalqaro mijozlar bilan, ayniqsa Yevropa va Germaniyada, uzoq muddatli hamkorlik qurishni xohlayman.",
        bio_p3_de="Heute ist mein Ziel größer als jedes einzelne Projekt: Ich möchte langfristige Partnerschaften mit internationalen Kunden aufbauen — besonders in Europa und Deutschland.",
        chip1_en="Remote-Ready", chip1_ru="Готов к удалённой работе", chip1_uz="Masofadan ishlashga tayyor", chip1_de="Remote-bereit",
        chip2_en="Client-Focused", chip2_ru="Ориентирован на клиента", chip2_uz="Mijozga yo'naltirilgan", chip2_de="Kundenorientiert",
        chip3_en="Detail-Obsessed", chip3_ru="Внимателен к деталям", chip3_uz="Detallarga e'tiborli", chip3_de="Detailversessen",
        chip4_en="English & German Friendly", chip4_ru="Английский и немецкий — без проблем", chip4_uz="Ingliz va nemis tillarida erkin", chip4_de="Englisch & Deutsch kein Problem",
    )

    # --- Timeline ---
    entries = [
        dict(order=1, year="2023", title_en="First Lines of Code", description_en="Started learning HTML, CSS, JavaScript and Python fundamentals.",
             title_ru="Первые строки кода", description_ru="Начал изучать основы HTML, CSS, JavaScript и Python.",
             title_uz="Kodning birinchi qatorlari", description_uz="HTML, CSS, JavaScript va Python asoslarini o'rganishni boshladim.",
             title_de="Erste Zeilen Code", description_de="Begann mit den Grundlagen von HTML, CSS, JavaScript und Python."),
        dict(order=2, year="2024", title_en="First Freelance Projects", description_en="Delivered real client work: stores, websites, and interactive tools.",
             title_ru="Первые проекты на фрилансе", description_ru="Выполнил реальные заказы: магазины, сайты и интерактивные инструменты.",
             title_uz="Birinchi freelance loyihalar", description_uz="Haqiqiy mijozlar uchun do'konlar, saytlar va interaktiv vositalar yaratdim.",
             title_de="Erste Freelance-Projekte", description_de="Lieferte echte Kundenprojekte: Shops, Websites und interaktive Tools."),
        dict(order=3, year="2025", title_en="Full-Stack Growth", description_en="Expanded into full-stack architecture and pixel-perfect builds.",
             title_ru="Рост в Full-Stack", description_ru="Расширил навыки до full-stack архитектуры и точных по пикселям сайтов.",
             title_uz="Full-Stack o'sish", description_uz="Full-stack arxitektura va piksel darajasida aniq loyihalarga kengaydim.",
             title_de="Full-Stack-Wachstum", description_de="Erweiterte Kenntnisse in Full-Stack-Architektur und pixelgenauen Builds."),
        dict(order=4, year="Today", year_ru="Сегодня", year_uz="Bugun", year_de="Heute",
             title_en="Going Global", description_en="Building partnerships with international clients and tech communities.",
             title_ru="Выход на глобальный уровень", description_ru="Строю партнёрства с международными клиентами и tech-сообществами.",
             title_uz="Global darajaga chiqish", description_uz="Xalqaro mijozlar va tex-jamoalar bilan hamkorlik qurmoqdaman.",
             title_de="Global werden", description_de="Aufbau von Partnerschaften mit internationalen Kunden und Tech-Communities.",
             is_current=True),
    ]
    for e in entries:
        TimelineEntry.objects.create(**e)

    # --- Skills ---
    skills_data = [
        dict(order=1, name_en="Python", name_ru="Python", name_uz="Python", name_de="Python",
             description_en="Backend logic, automation, and scripting with clean, maintainable code.",
             description_ru="Бэкенд-логика, автоматизация и скрипты с чистым, поддерживаемым кодом.",
             description_uz="Backend mantiqi, avtomatlashtirish va skriptlar — toza, qo'llaniladigan kod bilan.",
             description_de="Backend-Logik, Automatisierung und Skripte mit sauberem, wartbarem Code.",
             icon="🐍", percentage=92, category="Backend"),
        dict(order=2, name_en="Django", name_ru="Django", name_uz="Django", name_de="Django",
             description_en="Full-stack web framework for building production-ready applications fast.",
             description_ru="Full-stack фреймворк для быстрой разработки production-ready приложений.",
             description_uz="Production darajasidagi ilovalarni tez yaratish uchun full-stack freymvork.",
             description_de="Full-Stack-Framework für schnelle Entwicklung produktionsreifer Anwendungen.",
             icon="🎸", percentage=88, category="Backend"),
        dict(order=3, name_en="JavaScript", name_ru="JavaScript", name_uz="JavaScript", name_de="JavaScript",
             description_en="Dynamic, interactive front-ends and logic that bring interfaces to life.",
             description_ru="Динамичные, интерактивные интерфейсы и логика, оживляющая продукт.",
             description_uz="Dinamik, interaktiv front-endlar va interfeyslarni tiriltiradigan mantiq.",
             description_de="Dynamische, interaktive Frontends und Logik, die Interfaces zum Leben erwecken.",
             icon="⚡", percentage=90, category="Frontend"),
        dict(order=4, name_en="HTML5", name_ru="HTML5", name_uz="HTML5", name_de="HTML5",
             description_en="Semantic, accessible markup as the structural foundation of every build.",
             description_ru="Семантическая, доступная разметка как основа любого проекта.",
             description_uz="Har bir loyihaning tarkibiy asosi sifatida semantik, kiruvchi belgilash.",
             description_de="Semantisches, zugängliches Markup als strukturelle Grundlage jedes Projekts.",
             icon="🌐", percentage=95, category="Frontend"),
        dict(order=5, name_en="CSS3", name_ru="CSS3", name_uz="CSS3", name_de="CSS3",
             description_en="Pixel-accurate layouts, animation, and visual polish across all devices.",
             description_ru="Точные по пикселям макеты, анимация и визуальный лоск на всех устройствах.",
             description_uz="Barcha qurilmalarda pikselga to'g'ri tartibler, animatsiya va vizual sayqallash.",
             description_de="Pixelgenaue Layouts, Animationen und visueller Feinschliff auf allen Geräten.",
             icon="🎨", percentage=93, category="Frontend"),
        dict(order=6, name_en="Tailwind CSS", name_ru="Tailwind CSS", name_uz="Tailwind CSS", name_de="Tailwind CSS",
             description_en="Utility-first styling for fast, consistent, production-grade interfaces.",
             description_ru="Утилитарный подход к стилям для быстрых и стабильных интерфейсов уровня production.",
             description_uz="Tez, barqaror va production darajasidagi interfeyslar uchun utility-first uslub.",
             description_de="Utility-First-Styling für schnelle, konsistente Interfaces auf Produktionsniveau.",
             icon="💨", percentage=91, category="Frontend"),
    ]
    for s in skills_data:
        Skill.objects.create(**s)

    # --- Social Links ---
    # NOTE: only real links carried over from the original project are
    # seeded here — no GitHub/LinkedIn/etc. placeholder URLs are invented.
    # Add real ones any time from Admin → Social Links.
    socials = [
        dict(order=1, platform="facebook",  url="https://www.facebook.com/profile.php?id=61585582575607", platform_name="Facebook"),
        dict(order=2, platform="instagram", url="https://www.instagram.com/developer.dox/", platform_name="Instagram"),
        dict(order=3, platform="telegram",  url="https://web.telegram.org/k/#777000", platform_name="Telegram"),
        dict(order=4, platform="kwork",     url="https://kwork.ru/user/developer_artur", platform_name="Kwork"),
    ]
    for s in socials:
        SocialLink.objects.create(**s)


def unseed(apps, schema_editor):
    pass  # no-op: forward-only seed


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_defaults, unseed),
    ]
