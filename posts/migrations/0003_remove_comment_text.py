# Generated by Django 4.1.3 on 2022-11-19 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
    ]
