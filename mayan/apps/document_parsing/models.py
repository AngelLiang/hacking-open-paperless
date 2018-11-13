from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from documents.models import DocumentPage, DocumentVersion

from .managers import DocumentPageContentManager


@python_2_unicode_compatible
class DocumentPageContent(models.Model):
    '''文档页码内容'''
    # 文档页码
    document_page = models.OneToOneField(
        DocumentPage, on_delete=models.CASCADE, related_name='content',
        verbose_name=_('Document page')
    )
    # 内容
    content = models.TextField(blank=True, verbose_name=_('Content'))

    objects = DocumentPageContentManager()

    def __str__(self):
        return force_text(self.document_page)

    class Meta:
        verbose_name = _('Document page content')
        verbose_name_plural = _('Document pages contents')


@python_2_unicode_compatible
class DocumentVersionParseError(models.Model):
    '''文档版本解析错误'''
    # 文档版本
    document_version = models.ForeignKey(
        DocumentVersion, on_delete=models.CASCADE,
        related_name='parsing_errors', verbose_name=_('Document version')
    )
    # 提交时间
    datetime_submitted = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name=_('Date time submitted')
    )
    # 结果
    result = models.TextField(blank=True, null=True, verbose_name=_('Result'))

    def __str__(self):
        return force_text(self.document_version)

    class Meta:
        ordering = ('datetime_submitted',)
        verbose_name = _('Document version parse error')
        verbose_name_plural = _('Document version parse errors')
