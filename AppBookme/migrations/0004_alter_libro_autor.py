# Generated by Django 5.0.6 on 2024-06-18 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBookme', '0003_alter_editoriales_libros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.CharField(max_length=40),
        ),
    ]
