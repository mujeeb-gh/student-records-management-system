# Generated by Django 4.2.4 on 2024-01-02 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='passport',
        ),
        migrations.AddField(
            model_name='student',
            name='passport_photo',
            field=models.ImageField(blank=True, null=True, upload_to='passport_photos/'),
        ),
    ]
