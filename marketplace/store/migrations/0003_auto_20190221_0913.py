# Generated by Django 2.1.7 on 2019-02-21 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_storeinvite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeinvite',
            name='role',
            field=models.CharField(choices=[('0', 'Staff'), ('1', 'Moderator')], default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='storemembers',
            name='role',
            field=models.CharField(choices=[('0', 'Staff'), ('1', 'Moderator')], default='0', max_length=1),
        ),
    ]