# Generated by Django 2.1.7 on 2019-02-26 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20190221_0913'),
        ('products', '0005_auto_20190226_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.Store'),
        ),
    ]