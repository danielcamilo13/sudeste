# Generated by Django 2.2.7 on 2019-11-28 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0013_auto_20191116_2331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cacamba',
            options={'verbose_name': '3. Cacamba'},
        ),
        migrations.AlterModelOptions(
            name='colaborador',
            options={'verbose_name': '2. Colaborador'},
        ),
        migrations.AlterModelOptions(
            name='identidadejuridica',
            options={'verbose_name': '1. Identidade Juridica'},
        ),
        migrations.AlterModelOptions(
            name='tipocacamba',
            options={'verbose_name': 'Tipos de Cacamba'},
        ),
        migrations.AlterField(
            model_name='tipocacamba',
            name='tpCacamba',
            field=models.CharField(choices=[('pole', 'pole'), ('rolon', 'rolon'), ('muk', 'muk')], max_length=15, null=True, verbose_name='Tipos de Cacambas'),
        ),
    ]
