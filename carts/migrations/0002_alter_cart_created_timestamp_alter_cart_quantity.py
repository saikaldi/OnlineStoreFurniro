# Generated by Django 5.0.6 on 2024-07-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added date'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Quantity'),
        ),
    ]
