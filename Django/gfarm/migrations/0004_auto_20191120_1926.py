# Generated by Django 2.1.7 on 2019-11-20 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gfarm', '0003_auto_20191120_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriaalimento',
            name='categoriaAlimento',
            field=models.FloatField(max_length=20, verbose_name=' Categoria do alimento '),
        ),
    ]
