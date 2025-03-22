# Generated by Django 4.2.20 on 2025-03-22 20:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0010_ip_image_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ip',
            old_name='ip',
            new_name='ip_address',
        ),
        migrations.RemoveField(
            model_name='image',
            name='views',
        ),
        migrations.AddField(
            model_name='ip',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
