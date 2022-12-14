# Generated by Django 4.1.3 on 2022-11-28 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_alter_categoriaproducto_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categorias',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.categoriaproducto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(),
        ),
    ]
