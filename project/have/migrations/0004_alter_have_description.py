# Generated by Django 4.1.5 on 2023-02-21 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('have', '0003_have_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='have',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]