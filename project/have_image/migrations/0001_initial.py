# Generated by Django 4.1.5 on 2023-02-06 18:37

from django.db import migrations, models
import django.db.models.deletion
import have_image.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('have', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HaveImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to=have_image.models.post_directory_path)),
                ('have', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='have.have')),
            ],
        ),
    ]
