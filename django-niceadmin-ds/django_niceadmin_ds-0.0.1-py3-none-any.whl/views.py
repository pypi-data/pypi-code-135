from django.shortcuts import render, redirect
from _data import contents

from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.apps import apps

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.INFO)


def home(request):
    c = contents.context

    # _variables.scss에서 한글 폰트를 추가해주고 여기에 적절한 폰트 링크를 적용한다.
    c['font_link'] = "https://fonts.googleapis.com/css?" \
                     "family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Nunito:300,300i,400,400i,600,600i,700,700i" \
                     "|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i"

    c['breadcrumb'] = {
        "title": 'Dashboard',
        "subtitle": '',
        "p": '',
    }

    if c['show_examples']:
        # niceadmin examples를 위한 context
        c["sidebar_examples_small"] = {
            "components": [
                'alerts', 'accordion', 'badges', 'breadcrumbs', 'buttons', 'cards', 'carousel',
                'list_group', 'modal', 'tabs', 'pagination', 'progress', 'spinners', 'tooltips',
            ],
            "forms": ['form_elements', 'form_layouts', 'form_editors',  'form_validation'],
            "tables": ['general_tables', 'data_tables'],
            "charts": ['chart_js', 'apex_charts', 'e-charts'],
            "icons": ['bootstrap_icons', 'remix_icons', 'boxicons'],
        }

        c["sidebar_examples_big"] = {
            "pages": [
                ['profile', 'bi-person'],
                ['faq', 'bi-question-circle'],
                ['contact', 'bi-envelope'],
                ['register', 'bi-card-list'],
                ['login', 'bi-box-arrow-in-right'],
                ['error_404', 'bi-dash-circle'],
                ['blank', 'bi-file-earmark'],
            ],
        }

    logger.info(c)

    return render(request, 'niceadmin/index.html', c)


def examples(request, title, subtitle):
    c = contents.context
    c['breadcrumb'] = {
        "title": title,
        "subtitle": subtitle,
    }
    logger.info(c)
    return render(request, f'niceadmin/{title}/{subtitle}.html', c)


def register(request):
    c = contents.context
    logger.info(c)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        terms = request.POST['terms']

        user = User.objects.create_user(username, email, password)
        user.last_name = name
        user.save()
        messages.success(request, 'You have been logged in!')
        return redirect('niceadmin:home')
    else:
        return render(request, 'niceadmin/pages/register.html', c)


def login(request):
    c = contents.context
    logger.info(c)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(f"user auth: {user}")
        if user is not None:
            django_login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('niceadmin:home')
        else:
            messages.success(request, 'Error logged in - Please try again...')
            return redirect('niceadmin:pages:login')
    else:
        return render(request, 'niceadmin/pages/login.html', c)


def logout(request):
    django_logout(request)
    return redirect('niceadmin:home')
