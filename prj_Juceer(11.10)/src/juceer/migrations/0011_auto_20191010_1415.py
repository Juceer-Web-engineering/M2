# Generated by Django 2.2.6 on 2019-10-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juceer', '0010_auto_20191010_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juceerpost',
            name='artist_id',
            field=models.CharField(default='herfB', max_length=100),
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='artist_name',
            field=models.CharField(default='osSRv', max_length=100),
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='artist_terms',
            field=models.CharField(default='oxrWE', max_length=100),
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='song_id',
            field=models.SlugField(default='kP1dk', unique=True),
        ),
    ]
