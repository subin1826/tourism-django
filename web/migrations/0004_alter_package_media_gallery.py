# Generated by Django 5.1.3 on 2024-12-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_package_media_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='media_gallery',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='packages/media_gallery/'),
        ),
    ]