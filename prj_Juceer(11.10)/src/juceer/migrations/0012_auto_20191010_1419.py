# Generated by Django 2.2.6 on 2019-10-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juceer', '0011_auto_20191010_1415'),
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
            field=models.CharField(default='F6JUc', max_length=100),
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='artist_name',
            field=models.CharField(default='o8eHt', max_length=100),
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='artist_terms',
            field=models.CharField(default='2YCGF', max_length=100),
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='song_id',
            field=models.SlugField(default='6zxfM', unique=True),
        ),
    ]
