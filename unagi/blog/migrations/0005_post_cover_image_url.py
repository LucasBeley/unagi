# Generated by Django 5.0 on 2024-01-03 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_draft_post_hidden_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_image_url',
            field=models.URLField(blank=True, default=None, max_length=255, null=True, verbose_name='cover_image_url'),
        ),
    ]
