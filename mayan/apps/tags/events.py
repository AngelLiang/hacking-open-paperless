from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _

from events.classes import Event

# 标签绑定事件
event_tag_attach = Event(
    name='tag_attach',
    label=_('Tag attached to document')
)
# 标签移除事件
event_tag_remove = Event(
    name='tag_remove',
    label=_('Tag removed from document')
)
