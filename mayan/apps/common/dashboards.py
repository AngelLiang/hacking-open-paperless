from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from .classes import Dashboard

# 主页
dashboard_main = Dashboard(name='main', label=_('Main'))
