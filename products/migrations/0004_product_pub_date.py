# Generated by Django 3.0.7 on 2020-07-10 03:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200710_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pub_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
