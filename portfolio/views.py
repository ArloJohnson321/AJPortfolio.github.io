from django.shortcuts import render


def home(request):
    context = {
        'name': 'Alex Johnson',
        'title': 'Django Developer & Problem Solver',
        'about': (
            'I build practical web products with clean UX and maintainable backend systems. '
            'I enjoy turning rough ideas into polished tools people rely on daily.'
        ),
        'skills': ['Django', 'Python', 'REST APIs', 'PostgreSQL', 'Docker'],
        'projects': [
            {
                'name': 'TaskFlow Pro',
                'description': 'A team task manager with real-time updates and custom workflows.',
                'tech': 'Django, Channels, Redis',
            },
            {
                'name': 'ShopPulse Analytics',
                'description': 'An ecommerce dashboard for conversion, retention, and sales forecasting.',
                'tech': 'Django, Celery, PostgreSQL',
            },
            {
                'name': 'ResumeForge',
                'description': 'A resume builder that exports polished PDF templates in seconds.',
                'tech': 'Django, HTMX, WeasyPrint',
            },
        ],
        'contact': {
            'email': 'alex@example.com',
            'github': 'https://github.com/alexjohnson',
            'linkedin': 'https://linkedin.com/in/alexjohnson',
        },
    }
    return render(request, 'portfolio/home.html', context)
