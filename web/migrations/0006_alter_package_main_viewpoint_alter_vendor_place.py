# Generated by Django 5.1.3 on 2024-12-10 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_package_description_alter_package_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='main_viewpoint',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='place',
            field=models.CharField(max_length=100),
        ),
    ]