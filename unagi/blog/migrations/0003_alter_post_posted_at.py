# Generated by Django 5.0 on 2023-12-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_delete_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted_at',
            field=models.DateTimeField(default=None, null=True, verbose_name='posted_at'),
        ),
    ]
