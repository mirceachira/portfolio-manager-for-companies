# Generated by Django 3.0.11 on 2020-12-17 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text="company's name")),
                ('description', models.TextField(help_text='description of the company')),
                ('email', models.TextField(help_text="company's email")),
                ('phone', models.TextField(help_text="company's phone")),
                ('adress', models.TextField(help_text="company's adress")),
            ],
        ),
    ]
