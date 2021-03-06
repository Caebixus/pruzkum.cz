# Generated by Django 3.2.6 on 2021-08-21 11:18

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='homepage_description',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='homepage_left_subtitle_description',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='homepage_left_subtitle_h2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='homepage_left_subtitle_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='homepage_left_subtitle_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='homepage_right_subtitle_description',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='homepage_right_subtitle_h2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='homepage_right_subtitle_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='homepage_right_subtitle_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='homepage_title_h1',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
