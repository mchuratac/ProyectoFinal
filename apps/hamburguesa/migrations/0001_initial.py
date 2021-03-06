# Generated by Django 2.2.7 on 2019-12-05 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoPedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoIngrediente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cliente', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_pedido', models.DateTimeField()),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=16)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamburguesa.EstadoPedido')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=16)),
                ('cantidad', models.IntegerField(default=1)),
                ('imagen', models.ImageField(null=True, upload_to='pictures/%y')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamburguesa.TipoIngrediente')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(default=1)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=16)),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamburguesa.Ingrediente')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamburguesa.Pedido')),
            ],
        ),
    ]
