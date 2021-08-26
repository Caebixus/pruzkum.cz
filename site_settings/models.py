from django.db import models
from wagtail.core import blocks
from streams import blocks

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page


@register_setting
class FooterNastaveni(BaseSetting):

    email = models.CharField(blank=True, null=True, max_length=30)
    phone = models.CharField(blank=True, null=True, max_length=30)
    text = models.CharField(blank=True, null=True, max_length=200)
    adress = models.CharField(blank=True, null=True, max_length=200)

    panels = [
        MultiFieldPanel([
            FieldPanel("email"),
            FieldPanel("phone"),
            FieldPanel("text"),
            FieldPanel("adress"),
        ], heading="Footer informace")
    ]

    template = "home/footer.html"

@register_setting
class HeaderMenuNastaveni(BaseSetting):

    content = StreamField(
        [
            ("menu", blocks.HeaderMenuBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content")
    ]

    template = "home/footer.html"
