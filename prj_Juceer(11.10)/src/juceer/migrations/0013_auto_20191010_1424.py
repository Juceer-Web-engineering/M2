# Generated by Django 2.2.6 on 2019-10-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juceer', '0012_auto_20191010_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juceerpost',
            name='artist_id',
            field=models.CharField(default='haes8', max_length=100),
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='artist_name',
            field=models.CharField(default='IuOac', max_length=100),
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='artist_terms',
            field=models.CharField(default='n6lbc', max_length=100),
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='song_id',
            field=models.SlugField(default='w9sBE', unique=True),
        ),
    ]
