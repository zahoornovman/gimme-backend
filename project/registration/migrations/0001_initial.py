# Generated by Django 4.1.5 on 2023-02-06 18:37

from django.db import migrations, models
import registration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=registration.models.code_generator)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
