# Generated by Django 3.2.13 on 2022-05-12 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_auto_20220430_0238'),
    ]

    operations = [
       
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
    ]
