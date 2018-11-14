from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _

from events.classes import Event

# 文件创建事件
event_document_create = Event(
    name='documents_document_create', label=_('Document created')
)
# 文档下载事件
event_document_download = Event(
    name='documents_document_download',
    label=_('Document downloaded')
)
# 文档属性编辑事件
event_document_properties_edit = Event(
    name='documents_document_edit', label=_('Document properties edited')
)
# 文档类型改变
event_document_type_change = Event(
    name='documents_document_type_change', label=_('Document type changed')
)
# 文档新版本事件
event_document_new_version = Event(
    name='documents_document_new_version', label=_('New version uploaded')
)
# 文档版本回复事件
event_document_version_revert = Event(
    name='documents_document_version_revert',
    label=_('Document version reverted')
)
# 文档查看事件
event_document_view = Event(
    name='documents_document_view',
    label=_('Document viewed')
)
