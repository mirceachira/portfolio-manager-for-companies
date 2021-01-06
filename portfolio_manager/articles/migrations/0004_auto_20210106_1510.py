# Generated by Django 3.0.11 on 2021-01-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20201223_1929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-publish_date',)},
        ),
        migrations.RemoveField(
            model_name='article',
            name='is_promoted',
        ),
        migrations.RemoveField(
            model_name='historicalarticle',
            name='is_promoted',
        ),
        migrations.AddField(
            model_name='article',
            name='is_pinned',
            field=models.BooleanField(default=False, help_text='should be displayed in the pinned articles section'),
        ),
        migrations.AddField(
            model_name='historicalarticle',
            name='is_pinned',
            field=models.BooleanField(default=False, help_text='should be displayed in the pinned articles section'),
        ),
    ]
