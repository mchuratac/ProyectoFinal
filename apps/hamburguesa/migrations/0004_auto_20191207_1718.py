# Generated by Django 2.2.7 on 2019-12-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamburguesa', '0003_auto_20191207_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingrediente',
            name='tipo',
        ),
        migrations.AddField(
            model_name='tipoingrediente',
            name='ingrediente',
            field=models.ManyToManyField(to='hamburguesa.Ingrediente'),
        ),
    ]
