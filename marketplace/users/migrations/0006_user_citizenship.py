# Generated by Django 2.0.5 on 2018-10-29 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0005_auto_20181029_1552")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="citizenship",
            field=models.CharField(blank=True, max_length=100, null=True),
        )
    ]
