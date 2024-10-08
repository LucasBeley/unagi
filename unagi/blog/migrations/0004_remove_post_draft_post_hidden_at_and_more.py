# Generated by Django 5.0 on 2023-12-30 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_posted_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='draft',
        ),
        migrations.AddField(
            model_name='post',
            name='hidden_at',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='hidden_at'),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_at',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='posted_at'),
        ),
    ]
