# Generated by Django 2.1.7 on 2019-02-27 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20190227_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='u_name',
        ),
    ]