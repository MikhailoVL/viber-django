# Generated by Django 2.2.4 on 2019-08-23 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viber', '0003_viberuser_viber_api_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viberuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
