# Generated by Django 5.0.6 on 2024-06-22 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBookme', '0008_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='reseñas',
            name='calificacion',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reseñas',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
