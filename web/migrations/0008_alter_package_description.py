# Generated by Django 5.1.3 on 2024-12-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_package_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
