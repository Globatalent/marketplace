# Generated by Django 2.0.5 on 2018-10-11 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("purchases", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="purchase",
            name="amount",
            field=models.PositiveIntegerField(
                help_text="amount of tokens purchased by the user"
            ),
        )
    ]
