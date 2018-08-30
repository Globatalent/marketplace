# Generated by Django 2.0.5 on 2018-08-23 10:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('athletes', '0009_athlete_biography'),
        ('supporters', '0009_auto_20180821_0830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('amount', models.PositiveIntegerField(help_text='amount of tokens purchaed by the supporter')),
                ('total', models.FloatField(help_text='total paid for the amount of tokens')),
                ('supporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='supporters.Supporter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('amount', models.PositiveIntegerField(help_text='amount of tokens issued by the athlete')),
                ('price', models.FloatField(help_text='total price for the amount of tokens issued')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to='athletes.Athlete')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='purchase',
            name='token',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='tokens.Token'),
        ),
    ]