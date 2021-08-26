""" Flexible page """

from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page

from streams import blocks

class FlexPage(Page):
    """ Flexible page class """

    about_us_title = models.CharField(max_length=40, null=True, blank=True)
    about_us_description = RichTextField(features=["bold", "italic"], blank=True, null=True)

    template = "flex/flex_page.html"

    content = StreamField(
        [
            ("cards", blocks.CardBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("about_us_title"),
        FieldPanel("about_us_description"),
        StreamFieldPanel("content")
    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
