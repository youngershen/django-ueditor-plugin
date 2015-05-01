from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.
class UeditorFile(models.Model):

    UPLOAD_SUCCEED = 0
    UPLOAD_FAILED = 1
    UPLOAD_STATUS = (
        (UPLOAD_SUCCEED, _('upload succeed')),
        (UPLOAD_FAILED, _('upload failed'))
    )

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    deleted_at = models.DateTimeField(_('deleted at'), blank=True, null=True)
    name = models.CharField(_('filename'), max_length=255)
    type = models.CharField(_('file type'), max_length=255, null=True, blank=True)
    url = models.CharField(_('url'), max_length=255, blank=True, null=True)
    status = models.IntegerField(_('status'), choices=UPLOAD_STATUS, default=UPLOAD_SUCCEED)

    class Meta:
        verbose_name = _('file')
        verbose_name_plural = _('files')
        ordering = ['-created_at']