# Generated by Django 3.2.6 on 2021-08-22 11:04

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('site_settings', '0002_rename_socialmediasettings_footernastaveni'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderMenuNastaveni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', wagtail.core.fields.StreamField([('menu', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(max_length=20, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=True)), ('button_url', wagtail.core.blocks.URLBlock(required=True))]))], blank=True, null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]