# Generated by Django 3.0.11 on 2021-02-12 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20210212_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='short_description',
            field=models.TextField(default='short fucking description for fucking articles', help_text='short description of the company, appears in list of companies'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalarticle',
            name='short_description',
            field=models.TextField(default='fuckin 2', help_text='short description of the company, appears in list of companies'),
            preserve_default=False,
        ),
    ]
