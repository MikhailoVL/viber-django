# Generated by Django 2.2.4 on 2019-08-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_nomber',
            field=models.CharField(default='', max_length=32),
        ),
    ]