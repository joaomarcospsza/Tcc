# Generated by Django 2.1.7 on 2019-11-20 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimentacao', '0002_entrada_medicamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada_medicamento',
            name='quantidade_estoque_atual',
        ),
    ]
