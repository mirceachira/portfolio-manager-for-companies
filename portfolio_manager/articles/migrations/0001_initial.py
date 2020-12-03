# Generated by Django 3.0.11 on 2020-12-03 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(help_text='the article title')),
                ('content', models.TextField(help_text='the article content')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Date the article was created')),
                ('publish_date', models.DateTimeField(help_text='Date the article was published')),
                ('is_approved', models.BooleanField(help_text='was this approved by an admin for publishing')),
                ('author', models.ForeignKey(help_text='article author', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
