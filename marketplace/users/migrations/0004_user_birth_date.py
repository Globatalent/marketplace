# Generated by Django 2.0.5 on 2018-10-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181011_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='birth date'),
        ),
    ]
