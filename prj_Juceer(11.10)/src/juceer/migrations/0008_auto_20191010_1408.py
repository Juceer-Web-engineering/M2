# Generated by Django 2.2.6 on 2019-10-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juceer', '0007_auto_20191010_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juceerpost',
            name='artist_id',
            field=models.CharField(default='AzXuu', max_length=100),
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='artist_name',
            field=models.CharField(default='ezvJI', max_length=100),
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='artist_terms',
            field=models.CharField(default='BuAeP', max_length=100),
        ),
        migrations.AlterField(
            model_name='juceerpost',
            name='song_id',
            field=models.SlugField(default='YFQdT', unique=True),
        ),
    ]
