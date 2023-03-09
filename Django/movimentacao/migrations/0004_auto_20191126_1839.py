# Generated by Django 2.1.7 on 2019-11-26 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gfarm', '0006_auto_20191126_1839'),
        ('movimentacao', '0003_remove_entrada_medicamento_quantidade_estoque_atual'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada_Alimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_entrada', models.FloatField()),
                ('alimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.Alimento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='entrada_medicamento',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
