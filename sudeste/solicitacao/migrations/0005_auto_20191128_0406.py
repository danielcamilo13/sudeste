# Generated by Django 2.2.7 on 2019-11-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0004_auto_20191128_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservico',
            name='dsOS',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='ordemservico',
            name='nmColaborador',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='colaborador'),
        ),
        migrations.AlterField(
            model_name='ordemservico',
            name='tpOperacao',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Tipo de Operação'),
        ),
    ]
