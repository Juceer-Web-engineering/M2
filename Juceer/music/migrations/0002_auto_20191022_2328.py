# Generated by Django 2.2.6 on 2019-10-22 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicpost',
            name='artist_id',
            field=models.CharField(default='2WIyBplXXdgCv4fz0', max_length=100),
        ),
        migrations.AlterField(
            model_name='musicpost',
            name='artist_name',
            field=models.CharField(default='sNX9Z', max_length=100),
        ),
        migrations.AlterField(
            model_name='musicpost',
            name='artist_terms',
            field=models.CharField(default='PVuaU', max_length=100),
        ),
        migrations.AlterField(
            model_name='musicpost',
            name='song_id',
            field=models.SlugField(default='FU7BGO09LZRppSK2q', unique=True),
        ),
    ]
