# Generated by Django 3.1.3 on 2020-12-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_auto_20201205_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]