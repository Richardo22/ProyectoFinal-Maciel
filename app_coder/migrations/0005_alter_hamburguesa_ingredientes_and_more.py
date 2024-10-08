# Generated by Django 5.1.1 on 2024-09-25 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0004_alter_empanada_ingredientes_alter_empanada_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburguesa',
            name='ingredientes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='hamburguesa',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hamburguesa',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='ingredientes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
