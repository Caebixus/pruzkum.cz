from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    templates = "home/home_page.html"

    max_count = 1

    homepage_title_h1 = models.CharField(max_length=50, blank=False, null=True)
    homepage_description = RichTextField(features=["bold", "italic"], blank=True, null=True)

    homepage_left_subtitle_h2 = models.CharField(max_length=50, blank=False, null=True)
    homepage_left_subtitle_description = RichTextField(features=["bold", "italic"], blank=True, null=True)
    homepage_left_subtitle_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    homepage_left_subtitle_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    homepage_right_subtitle_h2 = models.CharField(max_length=50, blank=False, null=True)
    homepage_right_subtitle_description = RichTextField(features=["bold", "italic"], blank=True, null=True)
    homepage_right_subtitle_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    homepage_right_subtitle_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("homepage_title_h1"),
        FieldPanel("homepage_description"),
        FieldPanel("homepage_left_subtitle_h2"),
        FieldPanel("homepage_left_subtitle_description"),
        ImageChooserPanel("homepage_left_subtitle_image"),
        PageChooserPanel("homepage_left_subtitle_link"),
        FieldPanel("homepage_right_subtitle_h2"),
        FieldPanel("homepage_right_subtitle_description"),
        ImageChooserPanel("homepage_right_subtitle_image"),
        PageChooserPanel("homepage_right_subtitle_link"),
        ]
