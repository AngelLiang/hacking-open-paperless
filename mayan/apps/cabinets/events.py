from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _

from events.classes import Event

# 柜子添加文档事件
event_cabinets_add_document = Event(
    name='cabinets_add_document',
    label=_('Document added to cabinet')
)
# 柜子移除文档事件
event_cabinets_remove_document = Event(
    name='cabinets_remove_document',
    label=_('Document removed from cabinet')
)
