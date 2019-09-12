# Generated by Django 2.2.4 on 2019-09-11 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viber', '0007_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViberUserStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(-1, 'default'), (0, 'subscribed'), (1, 'unsubscribed'), (2, 'getfone')], default=0)),
                ('viber_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viber.ViberUser')),
            ],
        ),
    ]
