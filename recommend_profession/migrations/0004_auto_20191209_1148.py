# Generated by Django 2.2.5 on 2019-12-09 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_profession', '0003_auto_20191125_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='profession',
            name='show1',
            field=models.CharField(default='', max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profession',
            name='show2',
            field=models.CharField(default='', max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profession',
            name='show3',
            field=models.CharField(default='', max_length=2048),
            preserve_default=False,
        ),
    ]
