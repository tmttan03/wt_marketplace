# Generated by Django 2.1.7 on 2019-02-28 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_user_u_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_owner',
            field=models.BooleanField(default=True),
        ),
    ]
