# Generated by Django 4.1.5 on 2023-02-01 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('want', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='want',
            old_name='user_profile',
            new_name='author',
        ),
    ]
