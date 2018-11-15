from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from smart_settings import Namespace


namespace = Namespace(name='dynamic_search', label=_('Search'))
# 搜索结果长度限制配置
setting_limit = namespace.add_setting(
    global_name='SEARCH_LIMIT', default=100,
    help_text=_('Maximum amount search hits to fetch and display.')
)
