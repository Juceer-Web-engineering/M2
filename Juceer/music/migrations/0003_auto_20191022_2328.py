# Generated by Django 2.2.6 on 2019-10-22 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20191022_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicpost',
            name='artist_id',
            field=models.CharField(default='iZUueI5BMIzqtgrez', max_length=100),
        ),
        migrations.AlterField(
            model_name='musicpost',
            name='artist_name',
            field=models.CharField(default='xcTrc', max_length=100),
        ),
        migrations.AlterField(
            model_name='musicpost',
            name='artist_terms',
            field=models.CharField(default='MNbkd', max_length=100),
        ),
        migrations.AlterField(
            model_name='musicpost',
            name='song_id',
            field=models.SlugField(default='890TnlkrLQCbi3910', unique=True),
        ),
    ]
