# Generated by Django 2.0.5 on 2018-10-10 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("campaigns", "0001_initial"), ("users", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="following",
            field=models.ManyToManyField(
                blank=True,
                limit_choices_to={"is_draft": False},
                related_name="followers",
                to="campaigns.Campaign",
                verbose_name="following",
            ),
        )
    ]
