# Generated by Django 5.1.3 on 2024-12-09 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('place', models.CharField(default=0, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(default=0, max_length=100)),
                ('password', models.CharField(default=0, max_length=20)),
            ],
        ),
    ]