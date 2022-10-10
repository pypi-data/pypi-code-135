# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['create_drf_app',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name }}',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name }}.accounts',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.accounts.migrations',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages._distutils_hack',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.asgiref',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.backports',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.backports.zoneinfo',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.corsheaders',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.apps',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.ar',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.ar_DZ',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.az',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.bg',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.bn',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.bs',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.ca',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.cs',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.cy',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.da',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.de',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.de_CH',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.el',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.en',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.en_AU',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.en_GB',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.eo',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.es',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.es_AR',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.es_CO',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.es_MX',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.es_NI',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.es_PR',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.et',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.eu',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.fa',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.fi',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.fr',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.fy',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.ga',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.gd',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.gl',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.he',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.hi',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.hr',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.hu',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.id',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.ig',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.is',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.it',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.ja',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.ka',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.km',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.kn',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.ko',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.ky',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.lt',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.lv',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.mk',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.ml',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.mn',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.ms',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.nb',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.nl',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.nn',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.pl',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.pt',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.pt_BR',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.ro',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.ru',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.sk',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.sl',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.sq',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.sr',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.sr_Latn',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.sv',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.ta',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.te',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.tg',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.th',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.tk',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.tr',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.uk',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.uz',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.vi',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.zh_Hans',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.locale.zh_Hant',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.conf.urls',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.admin',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.admin.migrations',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.admin.templatetags',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.admin.views',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.admindocs',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.auth',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.auth.handlers',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.auth.management',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.auth.management.commands',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.auth.migrations',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.contenttypes',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.contenttypes.management',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.contenttypes.management.commands',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.contenttypes.migrations',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.flatpages',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.flatpages.migrations',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.flatpages.templatetags',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.admin',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.db',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.db.backends',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.db.backends.base',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.db.backends.mysql',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.db.backends.oracle',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.db.backends.postgis',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.db.backends.spatialite',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.db.models',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.db.models.sql',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.forms',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.gdal',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.gdal.prototypes',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.gdal.raster',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.geoip2',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.geos',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.geos.prototypes',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.management',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.management.commands',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.serializers',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.sitemaps',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.gis.utils',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.humanize',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.humanize.templatetags',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.messages',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.messages.storage',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.postgres',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.postgres.aggregates',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.postgres.fields',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.postgres.forms',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.redirects',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.redirects.migrations',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.sessions',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.sessions.backends',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.sessions.management',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.sessions.management.commands',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.sessions.migrations',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.sitemaps',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.sitemaps.management',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.sitemaps.management.commands',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.sites',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.sites.migrations',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.staticfiles',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.staticfiles.management',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.staticfiles.management.commands',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.contrib.syndication',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.core',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.core.cache',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.core.cache.backends',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.core.checks',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.core.checks.compatibility',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.core.checks.security',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.core.files',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.core.handlers',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.core.mail',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.core.mail.backends',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.core.management',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.core.management.commands',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.core.serializers',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.core.servers',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.db',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.db.backends',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.db.backends.base',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.db.backends.dummy',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.db.backends.mysql',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.db.backends.oracle',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.db.backends.postgresql',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.db.backends.sqlite3',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.db.migrations',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.db.migrations.operations',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.db.models',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.db.models.fields',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.db.models.functions',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.db.models.sql',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.dispatch',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.forms',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.http',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.middleware',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.template',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.template.backends',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.template.loaders',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.templatetags',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.test',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.urls',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.utils',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.utils.translation',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.views',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.views.decorators',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.django.views.generic',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.jwt',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.cli',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.commands',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.distributions',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.index',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.locations',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.metadata',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.metadata.importlib',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.models',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.network',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.operations',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.operations.build',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.operations.install',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.req',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.resolution',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.resolution.legacy',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.resolution.resolvelib',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.utils',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._internal.vcs',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.cachecontrol',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.cachecontrol.caches',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.certifi',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.chardet',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.chardet.cli',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.chardet.metadata',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.colorama',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.distlib',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.distro',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.idna',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.msgpack',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.packaging',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.pep517',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.pep517.in_process',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.pkg_resources',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.platformdirs',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.pygments',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.pygments.filters',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.pygments.formatters',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.pygments.lexers',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.pygments.styles',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.pyparsing',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.pyparsing.diagram',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.requests',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.resolvelib',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.resolvelib.compat',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.rich',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.tenacity',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.tomli',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.urllib3',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.urllib3.contrib',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.urllib3.contrib._securetransport',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.urllib3.packages',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.urllib3.packages.backports',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.urllib3.util',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pip._vendor.webencodings',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pkg_resources',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pkg_resources._vendor',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pkg_resources._vendor.importlib_resources',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pkg_resources._vendor.jaraco',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pkg_resources._vendor.jaraco.text',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pkg_resources._vendor.more_itertools',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pkg_resources._vendor.packaging',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pkg_resources._vendor.pyparsing',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pkg_resources._vendor.pyparsing.diagram',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pkg_resources.extern',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.pytz',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.rest_framework',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.rest_framework.authtoken',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.rest_framework.authtoken.management',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.rest_framework.authtoken.management.commands',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.rest_framework.authtoken.migrations',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.rest_framework.management',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.rest_framework.management.commands',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.rest_framework.schemas',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.rest_framework.templatetags',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.rest_framework.utils',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.rest_framework_simplejwt',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.rest_framework_simplejwt.token_blacklist',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.rest_framework_simplejwt.token_blacklist.management',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.rest_framework_simplejwt.token_blacklist.management.commands',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.rest_framework_simplejwt.token_blacklist.migrations',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools._distutils',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools._distutils.command',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools._vendor',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools._vendor.importlib_metadata',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools._vendor.importlib_resources',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools._vendor.jaraco',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools._vendor.jaraco.text',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools._vendor.more_itertools',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools._vendor.packaging',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools._vendor.pyparsing',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools._vendor.pyparsing.diagram',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools._vendor.tomli',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools.command',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools.config',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools.config._validate_pyproject',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.setuptools.extern',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.sqlparse',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.sqlparse.engine',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.sqlparse.filters',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.Africa',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.America',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.America.Argentina',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.America.Indiana',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.America.Kentucky',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.America.North_Dakota',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.Antarctica',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.Arctic',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.Asia',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.Atlantic',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.Australia',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.Brazil',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.Canada',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.Chile',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.Etc',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.Europe',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.Indian',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.Mexico',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.Pacific',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.tzdata.zoneinfo.US',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.wheel',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.wheel.cli',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.wheel.vendored',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.venv.Lib.site-packages.wheel.vendored.packaging',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name }}.venv.Scripts',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name }}.{{ '
 'cookiecutter.project_name }}',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name }}.{{ '
 'cookiecutter.project_name }}.settings']

package_data = \
{'': ['*'],
 'create_drf_app': ['templates/basic/*',
                    'templates/basic/{{ cookiecutter.project_name }}/venv/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/Django-4.1.dist-info/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/PyJWT-2.5.0.dist-info/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/asgiref-3.5.2.dist-info/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/backports.zoneinfo-0.2.1.dist-info/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/app_template/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/app_template/migrations/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/af/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ar/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ar_DZ/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ast/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/az/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/be/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/bg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/bn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/br/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/bs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ca/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/cs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/cy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/da/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/de/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/dsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/el/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/en/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/en_AU/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/en_GB/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/eo/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/es/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/es_AR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/es_CO/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/es_MX/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/es_VE/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/et/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/eu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/fa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/fi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/fr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/fy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ga/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/gd/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/gl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/he/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/hi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/hr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/hsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/hu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/hy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ia/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/id/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ig/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/io/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/is/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/it/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ja/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ka/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/kab/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/kk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/km/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/kn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ko/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ky/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/lb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/lt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/lv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/mk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ml/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/mn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/mr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ms/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/my/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/nb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ne/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/nl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/nn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/os/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/pa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/pl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/pt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/pt_BR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ro/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ru/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/sk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/sl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/sq/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/sr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/sr_Latn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/sv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/sw/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ta/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/te/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/tg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/th/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/tk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/tr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/tt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/udm/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/uk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/ur/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/uz/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/vi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/zh_Hans/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/locale/zh_Hant/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/project_template/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/conf/project_template/project_name/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/af/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/am/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ar/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ar_DZ/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ast/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/az/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/be/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/bg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/bn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/br/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/bs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ca/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/cs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/cy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/da/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/de/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/dsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/el/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/en/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/en_AU/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/en_GB/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/eo/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/es/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/es_AR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/es_CO/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/es_MX/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/es_VE/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/et/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/eu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/fa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/fi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/fr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/fy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ga/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/gd/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/gl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/he/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/hi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/hr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/hsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/hu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/hy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ia/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/id/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/io/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/is/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/it/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ja/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ka/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/kab/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/kk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/km/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/kn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ko/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ky/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/lb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/lt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/lv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/mk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ml/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/mn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/mr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ms/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/my/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/nb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ne/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/nl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/nn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/os/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/pa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/pl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/pt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/pt_BR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ro/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ru/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/sk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/sl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/sq/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/sr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/sr_Latn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/sv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/sw/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ta/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/te/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/tg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/th/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/tr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/tt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/udm/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/uk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/ur/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/uz/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/vi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/zh_Hans/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/locale/zh_Hant/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/static/admin/css/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/static/admin/css/vendor/select2/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/static/admin/fonts/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/static/admin/img/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/static/admin/img/gis/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/static/admin/js/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/static/admin/js/admin/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/static/admin/js/vendor/jquery/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/static/admin/js/vendor/select2/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/static/admin/js/vendor/select2/i18n/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/static/admin/js/vendor/xregexp/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/templates/admin/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/templates/admin/auth/user/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/templates/admin/edit_inline/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/templates/admin/includes/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/templates/admin/widgets/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admin/templates/registration/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/af/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ar/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ar_DZ/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ast/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/az/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/be/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/bg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/bn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/br/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/bs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ca/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/cs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/cy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/da/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/de/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/dsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/el/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/en/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/en_AU/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/en_GB/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/eo/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/es/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/es_AR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/es_CO/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/es_MX/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/es_VE/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/et/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/eu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/fa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/fi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/fr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/fy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ga/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/gd/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/gl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/he/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/hi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/hr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/hsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/hu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ia/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/id/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/io/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/is/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/it/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ja/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ka/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/kab/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/kk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/km/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/kn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ko/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ky/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/lb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/lt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/lv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/mk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ml/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/mn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/mr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ms/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/my/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/nb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ne/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/nl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/nn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/os/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/pa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/pl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/pt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/pt_BR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ro/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ru/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/sk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/sl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/sq/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/sr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/sr_Latn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/sv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/sw/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ta/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/te/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/tg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/th/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/tr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/tt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/udm/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/uk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/ur/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/vi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/zh_Hans/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/locale/zh_Hant/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/admindocs/templates/admin_doc/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/af/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ar/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ar_DZ/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ast/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/az/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/be/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/bg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/bn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/br/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/bs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ca/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/cs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/cy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/da/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/de/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/dsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/el/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/en/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/en_AU/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/en_GB/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/eo/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/es/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/es_AR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/es_CO/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/es_MX/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/es_VE/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/et/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/eu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/fa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/fi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/fr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/fy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ga/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/gd/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/gl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/he/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/hi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/hr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/hsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/hu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/hy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ia/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/id/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/io/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/is/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/it/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ja/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ka/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/kab/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/kk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/km/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/kn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ko/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ky/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/lb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/lt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/lv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/mk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ml/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/mn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/mr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ms/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/my/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/nb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ne/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/nl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/nn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/os/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/pa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/pl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/pt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/pt_BR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ro/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ru/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/sk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/sl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/sq/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/sr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/sr_Latn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/sv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/sw/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ta/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/te/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/tg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/th/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/tk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/tr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/tt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/udm/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/uk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/ur/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/uz/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/vi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/zh_Hans/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/locale/zh_Hant/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/templates/auth/widgets/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/auth/templates/registration/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/af/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ar/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ar_DZ/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ast/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/az/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/be/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/bg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/bn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/br/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/bs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ca/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/cs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/cy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/da/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/de/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/dsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/el/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/en/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/en_AU/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/en_GB/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/eo/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/es/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/es_AR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/es_CO/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/es_MX/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/es_VE/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/et/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/eu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/fa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/fi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/fr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/fy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ga/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/gd/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/gl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/he/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/hi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/hr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/hsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/hu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/hy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ia/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/id/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/io/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/is/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/it/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ja/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ka/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/kk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/km/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/kn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ko/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ky/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/lb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/lt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/lv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/mk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ml/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/mn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/mr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ms/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/my/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/nb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ne/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/nl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/nn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/os/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/pa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/pl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/pt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/pt_BR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ro/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ru/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/sk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/sl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/sq/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/sr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/sr_Latn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/sv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/sw/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ta/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/te/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/tg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/th/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/tk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/tr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/tt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/udm/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/uk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/ur/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/vi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/zh_Hans/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/contenttypes/locale/zh_Hant/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/af/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ar/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ar_DZ/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ast/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/az/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/be/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/bg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/bn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/br/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/bs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ca/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/cs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/cy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/da/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/de/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/dsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/el/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/en/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/en_AU/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/en_GB/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/eo/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/es/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/es_AR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/es_CO/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/es_MX/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/es_VE/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/et/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/eu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/fa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/fi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/fr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/fy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ga/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/gd/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/gl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/he/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/hi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/hr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/hsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/hu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/hy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ia/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/id/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/io/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/is/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/it/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ja/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ka/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/kk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/km/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/kn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ko/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ky/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/lb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/lt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/lv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/mk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ml/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/mn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/mr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ms/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/my/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/nb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ne/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/nl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/nn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/os/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/pa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/pl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/pt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/pt_BR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ro/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ru/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/sk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/sl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/sq/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/sr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/sr_Latn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/sv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/sw/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ta/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/te/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/tg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/th/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/tk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/tr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/tt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/udm/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/uk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/ur/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/vi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/zh_Hans/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/flatpages/locale/zh_Hant/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/af/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ar/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ar_DZ/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ast/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/az/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/be/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/bg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/bn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/br/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/bs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ca/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/cs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/cy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/da/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/de/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/dsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/el/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/en/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/en_AU/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/en_GB/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/eo/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/es/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/es_AR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/es_CO/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/es_MX/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/es_VE/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/et/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/eu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/fa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/fi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/fr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/fy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ga/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/gd/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/gl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/he/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/hi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/hr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/hsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/hu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/hy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ia/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/id/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/io/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/is/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/it/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ja/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ka/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/kk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/km/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/kn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ko/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ky/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/lb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/lt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/lv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/mk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ml/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/mn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/mr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ms/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/my/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/nb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ne/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/nl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/nn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/os/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/pa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/pl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/pt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/pt_BR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ro/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ru/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/sk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/sl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/sq/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/sr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/sr_Latn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/sv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/sw/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ta/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/te/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/tg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/th/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/tr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/tt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/udm/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/uk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/ur/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/vi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/zh_Hans/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/locale/zh_Hant/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/static/gis/css/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/static/gis/img/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/static/gis/js/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/templates/gis/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/templates/gis/admin/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/gis/templates/gis/kml/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/af/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ar/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ar_DZ/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ast/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/az/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/be/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/bg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/bn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/br/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/bs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ca/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/cs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/cy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/da/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/de/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/dsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/el/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/en/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/en_AU/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/en_GB/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/eo/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/es/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/es_AR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/es_CO/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/es_MX/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/es_VE/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/et/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/eu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/fa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/fi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/fr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/fy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ga/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/gd/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/gl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/he/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/hi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/hr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/hsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/hu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/hy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ia/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/id/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/io/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/is/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/it/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ja/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ka/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/kk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/km/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/kn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ko/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ky/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/lb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/lt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/lv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/mk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ml/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/mn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/mr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ms/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/my/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/nb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ne/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/nl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/nn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/os/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/pa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/pl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/pt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/pt_BR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ro/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ru/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/sk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/sl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/sq/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/sr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/sr_Latn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/sv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/sw/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ta/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/te/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/tg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/th/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/tr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/tt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/udm/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/uk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/ur/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/uz/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/vi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/zh_Hans/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/humanize/locale/zh_Hant/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/jinja2/postgres/widgets/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/af/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/ar/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/ar_DZ/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/az/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/be/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/bg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/ca/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/cs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/da/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/de/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/dsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/el/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/en/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/en_AU/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/eo/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/es/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/es_AR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/es_CO/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/es_MX/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/et/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/eu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/fa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/fi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/fr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/gd/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/gl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/he/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/hr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/hsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/hu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/hy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/ia/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/id/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/is/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/it/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/ja/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/ka/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/kk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/ko/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/ky/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/lt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/lv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/mk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/ml/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/mn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/ms/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/nb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/ne/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/nl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/nn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/pl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/pt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/pt_BR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/ro/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/ru/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/sk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/sl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/sq/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/sr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/sr_Latn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/sv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/tg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/tk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/tr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/uk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/uz/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/zh_Hans/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/locale/zh_Hant/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/postgres/templates/postgres/widgets/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/af/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ar/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ar_DZ/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ast/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/az/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/be/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/bg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/bn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/br/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/bs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ca/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/cs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/cy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/da/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/de/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/dsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/el/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/en/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/en_AU/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/en_GB/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/eo/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/es/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/es_AR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/es_CO/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/es_MX/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/es_VE/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/et/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/eu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/fa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/fi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/fr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/fy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ga/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/gd/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/gl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/he/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/hi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/hr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/hsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/hu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/hy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ia/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/id/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/io/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/is/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/it/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ja/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ka/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/kab/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/kk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/km/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/kn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ko/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ky/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/lb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/lt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/lv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/mk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ml/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/mn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/mr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ms/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/my/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/nb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ne/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/nl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/nn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/os/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/pa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/pl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/pt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/pt_BR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ro/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ru/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/sk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/sl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/sq/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/sr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/sr_Latn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/sv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/sw/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ta/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/te/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/tg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/th/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/tk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/tr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/tt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/udm/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/uk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/ur/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/uz/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/vi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/zh_Hans/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/redirects/locale/zh_Hant/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/af/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ar/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ar_DZ/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ast/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/az/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/be/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/bg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/bn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/br/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/bs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ca/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/cs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/cy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/da/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/de/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/dsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/el/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/en/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/en_AU/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/en_GB/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/eo/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/es/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/es_AR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/es_CO/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/es_MX/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/es_VE/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/et/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/eu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/fa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/fi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/fr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/fy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ga/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/gd/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/gl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/he/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/hi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/hr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/hsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/hu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/hy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ia/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/id/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/io/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/is/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/it/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ja/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ka/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/kab/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/kk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/km/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/kn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ko/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ky/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/lb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/lt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/lv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/mk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ml/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/mn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/mr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ms/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/my/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/nb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ne/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/nl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/nn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/os/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/pa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/pl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/pt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/pt_BR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ro/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ru/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/sk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/sl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/sq/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/sr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/sr_Latn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/sv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/sw/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ta/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/te/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/tg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/th/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/tk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/tr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/tt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/udm/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/uk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/ur/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/uz/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/vi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/zh_Hans/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sessions/locale/zh_Hant/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sitemaps/templates/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/af/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ar/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ar_DZ/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ast/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/az/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/be/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/bg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/bn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/br/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/bs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ca/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/cs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/cy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/da/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/de/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/dsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/el/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/en/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/en_AU/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/en_GB/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/eo/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/es/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/es_AR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/es_CO/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/es_MX/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/es_VE/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/et/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/eu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/fa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/fi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/fr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/fy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ga/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/gd/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/gl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/he/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/hi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/hr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/hsb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/hu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/hy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ia/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/id/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/io/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/is/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/it/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ja/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ka/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/kab/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/kk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/km/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/kn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ko/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ky/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/lb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/lt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/lv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/mk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ml/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/mn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/mr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ms/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/my/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/nb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ne/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/nl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/nn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/os/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/pa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/pl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/pt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/pt_BR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ro/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ru/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/sk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/sl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/sq/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/sr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/sr_Latn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/sv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/sw/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ta/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/te/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/tg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/th/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/tk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/tr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/tt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/udm/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/uk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/ur/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/uz/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/vi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/zh_Hans/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/contrib/sites/locale/zh_Hant/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/forms/jinja2/django/forms/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/forms/jinja2/django/forms/errors/dict/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/forms/jinja2/django/forms/errors/list/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/forms/jinja2/django/forms/formsets/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/forms/jinja2/django/forms/widgets/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/forms/templates/django/forms/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/forms/templates/django/forms/errors/dict/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/forms/templates/django/forms/errors/list/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/forms/templates/django/forms/formsets/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/forms/templates/django/forms/widgets/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django/views/templates/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/django_cors_headers-3.10.1.dist-info/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/djangorestframework-3.13.1.dist-info/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/djangorestframework_simplejwt-5.0.0.dist-info/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pip-22.2.2.dist-info/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz-2022.4.dist-info/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/Africa/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/America/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/America/Argentina/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/America/Indiana/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/America/Kentucky/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/America/North_Dakota/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/Antarctica/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/Arctic/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/Asia/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/Atlantic/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/Australia/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/Brazil/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/Canada/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/Chile/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/Etc/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/Europe/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/Indian/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/Mexico/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/Pacific/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/pytz/zoneinfo/US/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/ach/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/ar/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/az/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/be/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/bg/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/ca/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/ca_ES/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/cs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/da/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/de/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/el/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/el_GR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/en/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/en_AU/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/en_CA/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/en_US/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/es/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/et/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/fa/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/fa_IR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/fi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/fr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/fr_CA/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/gl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/gl_ES/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/he_IL/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/hu/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/hy/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/id/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/it/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/ja/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/ko_KR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/lt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/lv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/mk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/nb/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/ne_NP/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/nl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/nn/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/no/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/pl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/pt/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/pt_BR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/pt_PT/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/ro/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/ru/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/ru_RU/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/sk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/sl/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/sv/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/th/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/tr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/tr_TR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/uk/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/vi/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/zh_CN/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/zh_Hans/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/zh_Hant/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/locale/zh_TW/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/static/rest_framework/css/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/static/rest_framework/docs/css/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/static/rest_framework/docs/img/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/static/rest_framework/docs/js/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/static/rest_framework/fonts/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/static/rest_framework/img/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/static/rest_framework/js/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/templates/rest_framework/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/templates/rest_framework/admin/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/templates/rest_framework/docs/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/templates/rest_framework/docs/auth/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/templates/rest_framework/docs/langs/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/templates/rest_framework/filters/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/templates/rest_framework/horizontal/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/templates/rest_framework/inline/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/templates/rest_framework/pagination/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework/templates/rest_framework/vertical/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework_simplejwt/locale/cs/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework_simplejwt/locale/de_CH/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework_simplejwt/locale/es/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework_simplejwt/locale/es_AR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework_simplejwt/locale/es_CL/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework_simplejwt/locale/fa_IR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework_simplejwt/locale/fr/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework_simplejwt/locale/id_ID/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework_simplejwt/locale/it_IT/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework_simplejwt/locale/nl_NL/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework_simplejwt/locale/pl_PL/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework_simplejwt/locale/pt_BR/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework_simplejwt/locale/ru_RU/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework_simplejwt/locale/uk_UA/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/rest_framework_simplejwt/locale/zh_Hans/LC_MESSAGES/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/setuptools-65.3.0.dist-info/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/sqlparse-0.4.3.dist-info/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/tzdata-2022.4.dist-info/*',
                    'templates/basic/{{ cookiecutter.project_name '
                    '}}/venv/Lib/site-packages/wheel-0.37.1.dist-info/*']}

install_requires = \
['cookiecutter==2.1.1', 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['create-drf-app = create_drf_app.main:app']}

setup_kwargs = {
    'name': 'create-drf-app',
    'version': '0.1.21',
    'description': '',
    'long_description': '',
    'author': 'Mohammed Bajuaifer',
    'author_email': 'mohamadbajuaifer@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
