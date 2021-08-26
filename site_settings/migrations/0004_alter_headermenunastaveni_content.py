# Generated by Django 3.2.6 on 2021-08-22 11:05

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0003_headermenunastaveni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headermenunastaveni',
            name='content',
            field=wagtail.core.fields.StreamField([('menu', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(max_length=20, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False))]))], blank=True, null=True),
        ),
    ]