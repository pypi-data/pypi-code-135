from .views import *
from django.urls import path, re_path
from .validator import BasicValidator
from django.conf import settings


def add_pattern(model, form, form_update=False, validator=False, scripts=None, replace_fields=None):
    if scripts is None:
        scripts = {}

    if replace_fields is None:
        replace_fields = {}

    meta = model._meta
    app_label = meta.app_label
    model_name = meta.model_name

    gv.model_map[model_name] = model
    gv.validator_map[model_name] = validator or BasicValidator
    gv.scripts_map[model_name] = scripts
    gv.replace_fields[model_name] = replace_fields

    gv.ajax_form_map[app_label + '-' + 'add' + '-' + model_name] = form
    gv.ajax_form_map[app_label + '-' + 'change' + '-' + model_name] = form_update if form_update else form
    data_keys = ",".join(f.name for f in meta.get_fields())
    # print(data_keys)
    data_keys = 'id,' + data_keys.split('id,')[1]
    # print(data_keys)
    model_id = app_label + '-' + 'view' + '-' + model_name

    if gv.menu_map.get(app_label, 0):
        gv.menu_map[app_label]['submenu'].append({
            'id': model_id,
            'data_r_kwargs': '',
            'data_keys': data_keys,
            'title': meta.verbose_name.capitalize()
        })

    else:
        gv.menu_map[app_label] = {
            'app': app_label,
            'id': app_label + 'AppMenuItem',
            'title': app_label.capitalize(),
            'submenu': [
                {
                    'id': model_id,
                    'data_r_kwargs': '',
                    'data_keys': data_keys,
                    'title': meta.verbose_name.capitalize()
                }
            ]
        }

    gv.data_map_for_list_view[model_id] = {
        'r_kwargs': '',
        'data-keys': data_keys,
        'data-post-url': '/ajax/two-act-handler/'
    }

BASE_URL = getattr(settings, 'ONEPAGE_BASE_URL', '')

patterns = [
    path('ajax/four-act-handler/', ajax_four_act_handler, name='ajax-four-act-handler'),
    path('ajax/two-act-handler/', ajax_two_act_handler, name='ajax-two-act-handler'),
    path('onepage/set-session/', onepage_set_session, name='onepage-set-session'),
    path(BASE_URL, onepage_home, name='onepage-home'),
    re_path(r'^(?P<props>[\w-]+)/', ajax_four_act_handler, name="ajax-one-page-view")
]
