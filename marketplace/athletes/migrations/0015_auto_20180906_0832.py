# Generated by Django 2.0.5 on 2018-09-06 08:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('athletes', '0014_auto_20180906_0830'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('reviewer', 'athlete')},
        ),
    ]
