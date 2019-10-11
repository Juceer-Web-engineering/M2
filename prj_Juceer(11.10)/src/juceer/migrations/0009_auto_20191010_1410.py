# Generated by Django 2.2.6 on 2019-10-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juceer', '0008_auto_20191010_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juceerpost',
            name='publish_date',
        ),
        migrations.RemoveField(
            model_name='juceerpost',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='juceerpost',
            name='updated',
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='artist_id',
            field=models.CharField(default='UXEe5', max_length=100),
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='artist_name',
            field=models.CharField(default='pP2Bs', max_length=100),
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='artist_terms',
            field=models.CharField(default='y1uBl', max_length=100),
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='song_id',
            field=models.SlugField(default='Gq08C', unique=True),
        ),
    ]
