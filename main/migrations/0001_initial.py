# Generated by Django 5.0.6 on 2024-07-27 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=155, null=True, unique=True)),
            ],
        ),
    ]